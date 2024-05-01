import tkinter as tk #para que sea mas facil el uso de la libreria usamos el alias tk si no puesieramos esto tendriamos que poner tkiner a cada rato
from tkinter import messagebox #para las ventanas emergentes
from tkinter import ttk #para el estilo
import cone #para la coneccion ala base de datos
import ventanas #para poder cambiar de ventana
import sys #para obtener el valor de la variable usuario desde ventanas que se va pasando desde el main para saber que usuario es el que esta logeado

conexion = cone.conectar()#se crea la coneccion a la base de datos

def registrar():#para poder ir a registrar usuarios
    ventana.destroy()
    ventanas.registrar(usuarioactual)#se envia el valor que recibio por la linea de comandos

def registrarinv():#para poder ir a registrar inventario
    ventana.destroy()
    ventanas.reginventario(usuarioactual)#se envia el valor que recibio por la linea de comandos

def inv():#para poder ir a inventario
    ventana.destroy()
    ventanas.inventario(usuarioactual)#se envia el valor que recibio por la linea de comandos

def usuarios():#para poder ir a usuarios
    ventana.destroy()
    ventanas.usuarios(usuarioactual)#se envia el valor que recibio por la linea de comandos

def cambiarinv():#para poder ir a inventario
    ventana.destroy()
    ventanas.cambiarinv(usuarioactual) #se envia el valor que recibio por la linea de comandos

def usados():#para poder ir a usados
    ventana.destroy()
    ventanas.usados(usuarioactual) #se envia el valor que recibio por la linea de comandos

def generarreporte():#para poder ir a usados
    ventana.destroy()
    ventanas.generar(usuarioactual) #se envia el valor que recibio por la linea de comandos

def salir():#para cerrar sesion
    ventana.destroy()
    ventanas.principal(usuarioactual)#se envia el valor que recibio por la linea de comandos

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
ventana.title("Menu Principal Admin")
ventana.configure(bg="#835237")#color del fondo (background)

usuarioactual = sys.argv[1] #se resive el argumento pasado por la line a de comandos que se va pasando desde el main para saber que usuario es el que esta logeado

style = ttk.Style()#creacion de estilo
style.theme_use("clam")#eleccion de tema, tambien hay otros como defalut y alt

#Botón de cerrar sesion
boton_regresar = ttk.Button(ventana, text="Cerrar sesion", command=salir)
boton_regresar.pack(anchor="nw",padx= 5, pady=5)#anchor para colocarlo en la esquiina superior izquierda northwest

#botones del menu
boton_registrarusuarios = ttk.Button(ventana, text="Registrar Usuarios", command=registrar)
boton_registrarusuarios.pack(pady=(100,10))

boton_registrarinventario = ttk.Button(ventana, text="Registrar en inventario", command=registrarinv)
boton_registrarinventario.pack(pady=10)

boton_inventario = ttk.Button(ventana, text="Inventario", command=inv)
boton_inventario.pack(pady=10)

boton_inventario = ttk.Button(ventana, text="Usuarios", command=usuarios)
boton_inventario.pack(pady=10)

boton_inventario = ttk.Button(ventana, text="Usar o Agregar en inventario", command=cambiarinv)
boton_inventario.pack(pady=10)

boton_inventario = ttk.Button(ventana, text="Usados", command=usados)
boton_inventario.pack(pady=10)

boton_generar = ttk.Button(ventana, text="Generar reporte", command=generarreporte)
boton_generar.pack(pady=10)

#Ejecutar el bucle principal de la ventana
ventana.mainloop()#mainloop sirve para que ña ventana siga abierta y el usuario pueda interactuar con ella, para detenerla se debe destruir despues
