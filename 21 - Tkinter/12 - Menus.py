from tkinter import *

ventana = Tk()

#Menu principal
mimenu = Menu(ventana)
ventana.config(menu=mimenu)
ventana.geometry("300x200")

#Submenu archivos
archivo = Menu(mimenu,tearoff=0) #Tearoff --> evita que aparesca lina punteada
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir",command=ventana.quit)


#MENUS PRINCIPALES
mimenu.add_cascade(label="Archivos",menu=archivo) #Cascade para desprender menu
mimenu.add_command(label="Editar")
mimenu.add_command(label="Seleccion")
mimenu.add_command(label="Vista")

ventana.mainloop()