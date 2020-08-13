from tkinter import *
ventana = Tk()

texto = Label(ventana,text="Primer texto")
#fg--> color letra bg --> background "#000000" padx/y -->margen font-->fuente
texto.config(fg="white",
                bg="black",
                padx=60,
                pady=20,
                font=("arial black",20)
                )

texto.pack(side=TOP)
#with,height --> ancho,altura del texto --> medida de lineas
texto = Label(ventana,text="Primer texto")
texto.config(width = 5,
            height = 5,
            font = ("comic sans",20),
            bg="orange",
            cursor = "circle"   #arrow,spider
            )
#En el pad se espesifica la orientacion del texto
texto.pack(side=TOP,expand=YES,fill=X)




texto = Label(ventana,text="Prueba1")
texto.config(width = 10,
            height = 3,
            font = ("comic sans",10),
            bg="red",
            cursor = "circle"  
            )

texto.pack(side=LEFT,fill=X,expand=YES)

texto = Label(ventana,text="Prueba")
texto.config(width = 10,
            height = 3,
            font = ("comic sans",10),
            bg="green",
            cursor = "circle"  
            )
texto.pack(side=LEFT,fill=X,expand=YES)

texto.pack(anchor=CENTER)
texto = Label(ventana,text="Prueba")
texto.config(width = 10,
            height = 3,
            font = ("comic sans",10),
            bg="blue",
            cursor = "circle"  
            )

texto.pack(side=LEFT,fill=X,expand=YES)


ventana.mainloop()

