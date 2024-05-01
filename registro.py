import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el estilo
import cone #para la coneccion ala base de datos
import ventanas #para poder cambiar de ventana
import sys #para obtener el valor de la variable usuario desde ventanas que se va pasando desde el main para saber que usuario es el que esta logeado

conexion = cone.conectar()#se crea la coneccion a la base de datos

def regresar():#para poder regresar al menu
    ventana.destroy()#se destruye la ventana y se dirige al menu
    ventanas.menu(usuarioactual)#se tiene que seguir pasando el usuario

#creacion de la ventana para el registro de usuarios
ventana = tk.Tk()
ventana.geometry("800x650") #ajuste del ancho y alto respectivamente
#centrar ventana
ventana.update_idletasks()
ancho_ventana = ventana.winfo_width()#para saber el ancho de la pantalla
altura_ventana = ventana.winfo_height()#para saber el largo(altura) de la pantalla
x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)# // para hacer funcion piso bueno se redondea hacia abajo y queda como entero
y = (ventana.winfo_screenheight() // 2) - (altura_ventana // 2)
ventana.geometry('+{}+{}'.format(x, y - 30)) #sele resta 30 a y ya que es lo de la barra de tareas para que no afecte visualmente
ventana.title("Registro de usuarios")
ventana.configure(bg="#F56741")#color del fondo (background)

usuarioactual = sys.argv[1] #se resive el argumento pasado por la line a de comandos que se va pasando desde el main para saber que usuario es el que esta logeado

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

#Botón de menu
boton_regresar = ttk.Button(ventana, text="Menu", command=regresar)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

label_usuario = ttk.Label(ventana, text="Usuario")#para que muestre usuario
label_usuario.pack(pady=(100,5))#acomoda el label en la ventana, el pady sirve para aumentar el espaciado en la parte de arriba y de abajo, si se usan parentesis se especifica cual de las dos

entry_usuario = ttk.Entry(ventana)
entry_usuario.pack(pady=5)#acomoda el textfield en la ventana

label_nombre = ttk.Label(ventana, text="Nombre")#para que muestre usuario
label_nombre.pack(pady=5)#acomoda el label en la ventana

entry_nombre = ttk.Entry(ventana)
entry_nombre.pack(pady=5)#acomoda el textfield en la ventana

label_correo = ttk.Label(ventana, text="Correo")#para que muestre contraseña
label_correo.pack(pady=5)#acomoda el label en la ventana

entry_correo = ttk.Entry(ventana)
entry_correo.pack(pady=5)#acomoda el textfield en la ventana

label_contra = ttk.Label(ventana, text="Contraseña")#para que muestre contraseña
label_contra.pack(pady=5)#acomoda el label en la ventana

entry_contra = ttk.Entry(ventana, show="*")  # Para ocultar la contraseña
entry_contra.pack(pady=5)#acomoda el textfield en la ventana

label_contra2 = ttk.Label(ventana, text="Confirmar contraseña")#para que muestre contraseña
label_contra2.pack(pady=5)#acomoda el label en la ventana

entry_contra2 = ttk.Entry(ventana, show="*")  # Para ocultar la contraseña
entry_contra2.pack(pady=5)#acomoda el textfield en la ventana

opciones = ["admin", "usuario"]#lista de opciones para el Combobox
label_rol = ttk.Label(ventana, text="Rol")#para que muestre tipo
label_rol.pack(pady=5)#acomoda el label en la ventana, el pady sirve para aumentar el espaciado en la parte de arriba y de abajo, si se usan parentesis se especifica cual de las dos

combo_rol = ttk.Combobox(ventana, values=opciones)#se crea el combobox y como valores se le pone opciones
combo_rol.set(opciones[0])#para que aparesca ya con un valor
combo_rol.pack(pady=5)


#funcion para registrar en las tablas
def inertar_usuario(nombre, correo, usuario, contra, rol):
    cursor = conexion.cursor()#para poder hacer lñas consultas sql
    consulta = "INSERT INTO usuarios (nombre, correo, usuario, contra, rol) VALUES (%s, %s, %s, %s, %s)" #para insertar los valores, especificamos las columnas ya que la id se pondra automaticamente por lo que no es necesario ponerla
    cursor.execute(consulta, (nombre, correo, usuario, contra, rol))#ejecucion de la consulta
    conexion.commit()#para que se actualice la base de datos
    cursor.close()#para liberar recursos (memoria)


def registrar():
    usuario = entry_usuario.get()#para conseguir el texto escrito en los textfields
    contra = entry_contra.get()#para conseguir el texto escrito en los textfields
    contra2 = entry_contra2.get()#para conseguir el texto escrito en los textfields
    correo = entry_correo.get()#para conseguir el texto escrito en los textfields
    nombre = entry_nombre.get()#para conseguir el texto escrito en los textfields
    rol = combo_rol.get()#para saber que se selecciono
    #primero se comprueba que los entrys esten llenos
    if usuario and contra and contra2 and correo and nombre:
        if not cone.buscar(conexion, "usuarios", "usuario", usuario): #se3 comprueba que el usuario no este en la base de datos
            if not cone.buscar(conexion, "usuarios", "correo", correo): #se comprueba que el correo n este en la base de datos
                if contra == contra2: #se comprueba que las contraseñas coincidan
                    messagebox.showinfo("Registro exitoso", "{}, ha sido añadido".format(usuario))
                    inertar_usuario(nombre, correo, usuario, contra, rol)
                    #se regresa a la pagina de login
                    ventana.destroy()
                    ventanas.menu(usuarioactual)
                else:
                    messagebox.showerror("Contraseña incorrecta", "las contraseñas no coinciden")
            else:
                messagebox.showerror("Ya registrado", "Correo ya registrado, prueba con otro")
        else:
            messagebox.showerror("Ya registrado", "Usuario ya registrado, prueba con otro")
    else:
        messagebox.showerror("llena los campos", "No dejes campos vacios")

#Botón de registro
boton_registrar = ttk.Button(ventana, text="Registrar", command=registrar)
boton_registrar.pack(pady=5)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues
