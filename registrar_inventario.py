import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el combobox y los estilos
import cone #para la coneccion ala base de datos
import ventanas #para poder cambiar de ventana
import sys #para obtener el valor de la variable usuario desde ventanas que se va pasando desde el main para saber que usuario es el que esta logeado

conexion = cone.conectar()#se crea la coneccion a la base de datos


def regresar():#para poder regresar al menu
    ventana.destroy()#se destruye la ventana y se dirige al menu
    #se checa el ro, del usuario para saber a que menu ir
    querol = cone.valor_especifico(conexion, "usuarios", "rol", "usuario", usuarioactual) #se busca el rol usando el valor de usuario
    if querol[0] == "admin":
        ventanas.menu(usuarioactual)#se envia el valor que recibio por la linea de comandos
    else:#es usuario
        ventanas.menuus(usuarioactual)#se envia el valor que recibio por la linea de comandos

#creacion de la ventana para el registro de herramientas y materiales
ventana = tk.Tk()
ventana.geometry("800x650") #ajuste del ancho y alto respectivamente
#centrar ventana
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()#para saber el ancho de la pantalla
altura_ventana = ventana.winfo_height()#para saber el largo(altura) de la pantalla
x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)# // para hacer funcion piso bueno se redondea hacia abajo y queda como entero
y = (ventana.winfo_screenheight() // 2) - (altura_ventana // 2)
ventana.geometry('+{}+{}'.format(x, y - 30)) #sele resta 30 a y ya que es lo de la barra de tareas para que no afecte visualmente
ventana.title("Registro de herramientas y materiales")
ventana.configure(bg="#72E132")#color del fondo (background)

usuarioactual = sys.argv[1] #se resive el argumento pasado por la line a de comandos que se va pasando desde el main para saber que usuario es el que esta logeado

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

#Botón de menu
boton_regresar = ttk.Button(ventana, text="Menu", command=regresar)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

opciones = ["herramientas", "material"]#lista de opciones para el Combobox
label_tipo = ttk.Label(ventana, text="Tipo")#para que muestre tipo
label_tipo.pack(pady=(100,5))#acomoda el label en la ventana, el pady sirve para aumentar el espaciado en la parte de arriba y de abajo, si se usan parentesis se especifica cual de las dos

combo_tipo = ttk.Combobox(ventana, values=opciones)#se crea el combobox y como valores se le pone opciones
combo_tipo.set(opciones[0])#para que aparesca ya con un valor
combo_tipo.pack(pady=5)

label_nombre = ttk.Label(ventana, text="Nombre")#para que muestre nombre
label_nombre.pack(pady=5)#acomoda el label en la ventana

entry_nombre = ttk.Entry(ventana)
entry_nombre.pack(pady=5)#acomoda el textfield en la ventana

opciones2 = ["tornillos", "brocas", "llaves Allen", "Uso General"]#lista de opciones para el Combobox2
label_categoria = ttk.Label(ventana, text="Categoria")#para que muestre categoria
label_categoria.pack(pady=5)#acomoda el label en la ventana

combo_categoria = ttk.Combobox(ventana, values=opciones2)#se crea el combobox y como valores se le pone opciones
combo_categoria.set(opciones2[0])#para que aparesca ya con un valor
combo_categoria.pack(pady=5)

label_cantidad = ttk.Label(ventana, text="Cantidad")#para que muestre cantidad
label_cantidad.pack(pady=5)#acomoda el label en la ventana

entry_cantidad = ttk.Entry(ventana)
entry_cantidad.pack(pady=5)#acomoda el textfield en la ventana

label_medida = ttk.Label(ventana, text="Medida")#para que muestre medida
label_medida.pack(pady=5)#acomoda el label en la ventana

entry_medida = ttk.Entry(ventana) 
entry_medida.pack(pady=5)#acomoda el textfield en la ventana

label_minimo = ttk.Label(ventana, text="Minimo")#para que muestre minimo
label_minimo.pack(pady=5)#acomoda el label en la ventana

entry_minimo = ttk.Entry(ventana)  # Para ocultar la contraseña
entry_minimo.pack(pady=5)#acomoda el textfield en la ventana

#funcion para registrar en las tablas
def inertar_inventario(tabla, nombre, categoria, cantidad, medida, minimo):
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "INSERT INTO {} (nombre, categoria, cantidad, medida, minimo) VALUES (%s, %s, %s, %s, %s)".format(tabla) #para insertar los valores, especificamos las columnas ya que la id se pondra automaticamente por lo que no es necesario ponerla
    cursor.execute(consulta, (nombre, categoria, cantidad, medida, minimo))#ejecucion de la consulta
    conexion.commit()#para que se actualice la base de datos
    cursor.close()#para liberar recursos (memoria)


def registrar():
    tabla = combo_tipo.get()#para saber que se selecciono
    nombre = entry_nombre.get()#para conseguir el texto escrito en los textfields
    categoria = combo_categoria.get()#para saber que se selecciono
    cantidad = entry_cantidad.get()#para conseguir el texto escrito en los textfields
    medida = entry_medida.get()#para conseguir el texto escrito en los textfield
    minimo = entry_minimo.get()#para conseguir el texto escrito en los textfields

    cantidadusar = int(cantidad)
    minimousar = int(minimo)

    #se comprueba que todos los entrys tenga informacion
    if nombre and cantidad and medida and minimo:#si tienen informacion los textfields procede al registro
        if cantidad.isdigit():#se checa que se entero
            if minimo.isdigit():
                if (cantidadusar and minimousar) > 0:#se checa que cantidad y minimo no sean cantidades negativas
                    if not cone.buscar(conexion, tabla, "nombre", nombre): #se comprueba que el nombre no este en la base de datos
                        messagebox.showinfo("Registro exitoso", "{} {}, agregada".format(tabla, nombre))
                        inertar_inventario(tabla, nombre, categoria, cantidad, medida, minimo)#se manda a insertar
                    else:
                        messagebox.showerror("Ya registrado", "Usuario ya registrado")
                else:
                    messagebox.showerror("Cantidad erronea", "Cantidad y Minimo deben ser mayor que 0")
            else:
                messagebox.showerror("Cantidad erronea", "Minimo debe ser una cantidad entera")
        else:
            messagebox.showerror("Cantidad erronea", "Cantidad debe ser una cantidad entera")
    else:
        messagebox.showerror("llena los campos", "No dejes campos vacios")

#Botón de registro
boton_registrar = ttk.Button(ventana, text="Registrar", command=registrar)
boton_registrar.pack(pady=5)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues
