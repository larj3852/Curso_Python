from tkinter import Tk,Label,CENTER,E
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("400x300")


texto = Label(ventana,text="Hola mundo")
texto.pack(anchor=CENTER)

imagen = Image.open("./21 - Tkinter/Imagenes/pato.jpg")
render = ImageTk.PhotoImage(imagen)
#Para montar una imagen, hay que ponerlo en un render
Label(ventana,image=render).pack(anchor=E)

ventana.mainloop()