from tkinter import TK,Label
ventana = Tk()
ventana.geometry("600x400")



texto = Label(ventana,text="Primer texto")
#fg--> color letra bg --> background "#000000" padx/y -->margen font-->fuente
texto.config(fg="white",
                bg="black",
                padx=60,
                pady=20,
                font=("arial black",20)
                )

texto.pack() #Se carga dentro de la ventana

#with,height --> ancho,altura del texto --> medida de lineas
texto = Label(ventana,text="Primer texto")
texto.config(width = 10,
            height = 400,
            font = ("comic sans",20),
            bg="orange",
            cursor = "circle"   #arrow,spider
            )
#En el pad se espesifica la orientacion del texto
texto.pack(anchor=CENTER) #Se carga dentro de la ventana



ventana.mainloop()