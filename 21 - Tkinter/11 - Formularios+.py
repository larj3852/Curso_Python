from tkinter import *

def mostrarProfesion():
    texto = ""
    if web.get():
        texto+="Desarrollo web "
    if movil.get():
        texto+="Desarrollo movil "
    
    mostrar.config(text=texto, bg="green",fg="white")

ventana = Tk()
ventana.geometry("500x600")
web = IntVar()
movil = IntVar()


encabezado = Label(ventana,text="Formularios 'Avanzados' ")
encabezado.config(bg="green",fg="white",padx=60,pady=8)
encabezado.grid(row=0,column=0,sticky=N,columnspan=2)

#Botones: CHECKBOX
Label(ventana,text="Campo 1").grid(row=1,column=0,sticky=W)
Checkbutton(ventana,text="Desarrollador Web",
            variable=web,
            onvalue  = 1,
            offvalue = 0,
            command = mostrarProfesion
            ).grid(row=2,column=0,sticky=W)


Checkbutton(ventana,text="Desarrollador movil",
            variable=movil,
            onvalue=1,
            offvalue=0,
            command = mostrarProfesion
            ).grid(row=3,column=0,sticky=W)

mostrar = Label(ventana,text="")
mostrar.grid(row=4,column=0,sticky=W)


#RADIOBUTTOMS
opcion = StringVar()
opcion.set(None)
def marcar():
    marcado.config(text=opcion.get())

Label(ventana,text="¿Cual es tu género?: ").grid(row=4,column=0,sticky=W)

Radiobutton(ventana,text="Femenino",
            variable = opcion,
            value= "Femenino",
            command = marcar
            ).grid(row=5,column=0,sticky=W)

Radiobutton(ventana,text="Masculino",
            variable = opcion,
            value = "Masculino",
            command = marcar
            ).grid(row=6,column=0,sticky=W)

marcado=Label(ventana,text="")
marcado.grid(row=7,column=0,sticky=W)


#OPTION MENU
Label(ventana,text="OPTION MENU").grid(row=1,column=1,sticky=W)
opcion2= StringVar()

def select():
    seleccionado.config(text=opcion2.get())

opcion2.set("Opcion 1") #Opcion default
seleccion=OptionMenu(ventana,opcion2,"Opcion 1","Opcion 2","Opcion 3","Opcion 4")
seleccion.grid(row=3,column=1,sticky=W)

Button(ventana,text="Mostrar",command=select).grid(row=4,column=1,sticky=N)
seleccionado=Label(ventana,text="")
seleccionado.grid(row=5,column=1,sticky=W)

ventana.mainloop()