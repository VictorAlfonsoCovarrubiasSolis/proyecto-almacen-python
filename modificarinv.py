import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el combobox y los estilos
import cone #para la coneccion ala base de datos
import ventanas #para poder cambiar de ventana
import sys #para obtener el valor de la variable usuario desde ventanas que se va pasando desde el main para saber que usuario es el que esta logeado

conexion = cone.conectar()#se crea la coneccion a la base de datos


def regresar():#para poder regresar al menu del nivel del usuario
    ventana.destroy()#se destruye la ventana y se dirige al menu
    #se checa el ro, del usuario para saber a que menu ir
    querol = cone.valor_especifico(conexion, "usuarios", "rol", "usuario", usuarioactual) #se busca el rol usando el valor de usuario
    if querol[0] == "admin":
        ventanas.menu(usuarioactual)#se envia el valor que recibio por la linea de comandos
    else:#es usuario
        ventanas.menuus(usuarioactual)#se envia el valor que recibio por la linea de comandos

def regresar2():#para poder regresar al menu
    ventana.destroy()#se destruye la ventana y se dirige al menu
    ventanas.inventario(usuarioactual)#se tiene que seguir pasando el usuario

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
ventana.title("Modificacion herramientas y materiales")
ventana.configure(bg="#72E132")#color del fondo (background)

usuarioactual = sys.argv[1] #se resive el argumento pasado por la linea de comandos que se va pasando desde el main para saber que usuario es el que esta logeado
tabla = sys.argv[2] #se resive el segundo argumento pasado por la linea de comandos lo seleccionado en la tabla
invmod = sys.argv[3] #se resive el tercer argumento pasado por la linea de comandos lo seleccionado en la tabla

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

#se consiguen los datos de la herramienta o material seleccionado
categoriamod = cone.valor_especifico(conexion, tabla, "categoria", "nombre", invmod)#se consigue la categoria de lo seleccionado a modificar
cantidadmod = cone.valor_especifico(conexion, tabla, "cantidad", "nombre", invmod)#se consigue la cantidad de lo seleccionado a modificar
medidamod = cone.valor_especifico(conexion, tabla, "medida", "nombre", invmod)#se consigue la medida de lo seleccionado a modificar
minimomod = cone.valor_especifico(conexion, tabla, "minimo", "nombre", invmod)#se consigue el minimo de lo seleccionado a modificar

#Botón de menu
boton_regresar = ttk.Button(ventana, text="Menu", command=regresar)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

#Botón de inventario
boton_regresar = ttk.Button(ventana, text="Atras", command=regresar2)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

label_nombre = ttk.Label(ventana, text="Nombre")#para que muestre nombre
label_nombre.pack(pady=5)#acomoda el label en la ventana

entry_nombre = ttk.Entry(ventana)
entry_nombre.pack(pady=5)#acomoda el textfield en la ventana
entry_nombre.insert(0, invmod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no

opciones = ["tornillos", "brocas", "llaves Allen", "Uso General"]#lista de opciones para el Combobox2
label_categoria = ttk.Label(ventana, text="Categoria")#para que muestre categoria
label_categoria.pack(pady=5)#acomoda el label en la ventana

combo_categoria = ttk.Combobox(ventana, values=opciones)#se crea el combobox y como valores se le pone opciones
#para poner desde antes la categoria a la que pertenece
if categoriamod[0] == "tornillos":
    combo_categoria.set(opciones[0])#para que aparesca ya con un valor
elif categoriamod[0] == "brocas":
    combo_categoria.set(opciones[1])#para que aparesca ya con un valor
elif categoriamod[0] == "llaves Allen":
    combo_categoria.set(opciones[2])#para que aparesca ya con un valor
elif categoriamod[0] == "Uso General":
    combo_categoria.set(opciones[3])#para que aparesca ya con un valor
combo_categoria.pack(pady=5)

label_cantidad = ttk.Label(ventana, text="Cantidad")#para que muestre cantidad
label_cantidad.pack(pady=5)#acomoda el label en la ventana

entry_cantidad = ttk.Entry(ventana)
entry_cantidad.pack(pady=5)#acomoda el textfield en la ventana
entry_cantidad.insert(0, cantidadmod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no

label_medida = ttk.Label(ventana, text="Medida")#para que muestre medida
label_medida.pack(pady=5)#acomoda el label en la ventana

entry_medida = ttk.Entry(ventana) 
entry_medida.pack(pady=5)#acomoda el textfield en la ventana
entry_medida.insert(0, medidamod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no

label_minimo = ttk.Label(ventana, text="Minimo")#para que muestre minimo
label_minimo.pack(pady=5)#acomoda el label en la ventana

entry_minimo = ttk.Entry(ventana)  # Para ocultar la contraseña
entry_minimo.pack(pady=5)#acomoda el textfield en la ventana
entry_minimo.insert(0, minimomod)#se pone desde el principio el valor que tenia antes para que el usuario sepa que tenia y decida si cambiarlo o no

def modificar():
    nombre = entry_nombre.get()#para conseguir el texto escrito en los textfields
    categoria = combo_categoria.get()#para saber que se selecciono
    cantidad = entry_cantidad.get()#para conseguir el texto escrito en los textfields
    medida = entry_medida.get()#para conseguir el texto escrito en los textfield
    minimo = entry_minimo.get()#para conseguir el texto escrito en los textfields

    #primero se comprueba que los entrys esten llenos
    if nombre and cantidad and medida and minimo:#si tienen informacion los textfields procede al registro
        if cantidad.isdigit():#se checa que se entero
            if minimo.isdigit():
                if nombre != invmod and cone.buscar(conexion, tabla, "nombre", nombre): #se comprueba si es diferente el nombre que tiene el seleccionado al nombre a modificar y que el nombre este en la base de datos
                    messagebox.showerror("Ya registrado", "{} ya registrado, prueba con otro".format(tabla))
                else:
                    messagebox.showinfo("Cambio realizado", "se modifico {}: {}".format(tabla, nombre))
                    cone.modificarinv(conexion, tabla, invmod, nombre, categoria, cantidad, medida, minimo)#se manda a modificar
            else:
                messagebox.showerror("Cantidad erronea", "Minimo debe ser una cantidad entera")
        else:
            messagebox.showerror("Cantidad erronea", "Cantidad debe ser una cantidad entera")
    else:
        messagebox.showerror("llena los campos", "No dejes campos vacios")

#Botón de modificar
boton_registrar = ttk.Button(ventana, text="Modificar", command=modificar)
boton_registrar.pack(pady=5)


#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues
