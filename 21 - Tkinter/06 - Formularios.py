from tkinter import *

ventana= Tk()
ventana.geometry("500x500")
ventana.title("Formularios en Tkinter")

#Encabezado
Encabezado=Label(ventana,text="Formularios en TKinter")
Encabezado.config(bg="white",
                    fg="darkgray",
                    font=("Open Sans", 18),
                    padx=10,
                    pady=10
                    )
Encabezado.grid(row=0,column = 0, columnspan=3, sticky=W) #Si ocupo grid, no puedo usar pack

#Label para el campo NOMBRE
label = Label(ventana,text="Nombre")
label.grid(row=1,column=0, padx=5,pady=5, sticky=W)
#Label para el campo APELLIDOS
label = Label(ventana,text="Apellidos")
label.grid(row=2,column=0, padx=5,pady=5, sticky=W)


#CREACION campo de texto NOMBRE
campo_texto = Entry(ventana)
campo_texto.grid(row = 1,column = 1,padx=5,pady=5, sticky = W)
#CREACION campo de texto APELLIDOS
campo_texto2 = Entry(ventana)
campo_texto2.grid(row = 2,column = 1,padx=5,pady=5, sticky = W)
campo_texto2.config(justify="right",state="disable") 
        #state-->disable,normal
        #Justify --> entra de texto por derecha,izquierda

#Label para el campo TEXTO GRANDE
label = Label(ventana,text="Descripcion")
label.grid(row=3,column=0, padx=5,pady=5, sticky=NW)

campo_texto.grid(row = 1,column = 1,padx=5,pady=5, sticky = W)
#CAMPO TEXTO GRANDE P/ DESCRIPCION
campo_grande= Text(ventana)
campo_grande.grid(row=3,column=1)
campo_grande.config(width=30,
                    height=5, 
                    font=("Arial",12),
                    padx=15,
                    pady=15
                    )

#%% Botones
Label(ventana).grid(row=4,column=5)#Espaciado
boton = Button(ventana,text="Enviar")
boton.grid(row=5,column=1,sticky=E)
boton.config(bg="green",fg="white",padx=10,pady=4)









ventana.mainloop()
