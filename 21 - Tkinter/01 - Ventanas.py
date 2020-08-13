#Para ejecutar el programa, se debe de ejecutar desde la raiz y se debe poner las subcarpetas
#y shalala... 
from tkinter import Tk,Label
import os.path

#SE PUEDE CREAR UNA CLASE CONCRETA PARA EL PROGRAMA

class Programa:
    
    def __init__(self):
        self.title= "Primera aplicacion"
        self.icon =  '@/21 - Tkinter/Imagenes/imagen.xbm'
        self.size = "800x500"
        self.resizable = False

    def cargar(self):
        ventana = Tk()
        self.ventana=ventana
        ventana.geometry(self.size)
        if not self.resizable:
            ventana.resizable(1,1) 
        texto = Label(ventana,text=self.title)
        texto.pack()
        
    
    def addtexto(self,texto):
        texto = Label(self.ventana,text=texto)
        texto.pack()
    
    def mostar(self):
        self.ventana.mainloop()

#Iniciar Programa
programa = Programa()
programa.cargar()
programa.addtexto("Hola k hace")
programa.addtexto("Hola k hace")
programa.addtexto("Hola k hace")
programa.addtexto("Hola k hace")
programa.addtexto("Hola k hace")
programa.addtexto("Hola k hace")
programa.mostar()
"""        
#Crear ventana
ventana = Tk()
#Titulo
ventana.title("Primera interfaz grafica")


#comprobar si existe archivo
ruta_icono= os.path.abspath("./imagenes/imagen.xbm")  #Ruta absoluta
if not os.path.isfile(ruta_icono):
    ruta_icono = "@/21 - Tkinter/Imagenes/imagen.xbm"

#Icono 
#En windows .ico en linux .bmx
#   ventana.iconbitmap('@/21 - Tkinter/Imagenes/imagen.xbm')

#Redimencionar ventana
ventana.geometry("800x600")
#Bloquear tamañoo
ventana.resizable(0,0) #bloquear fila o columna con 0/1

#Mostrar texto en programa
texto = Label(ventana,text=ruta_icono)
texto.pack()
#Arrancar  y mostrar ventana hasta que se cierre
ventana.mainloop()
"""