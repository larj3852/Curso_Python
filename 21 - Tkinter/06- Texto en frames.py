from tkinter import *
import PIL
from PIL import ImageTk

ventana = Tk()
ventana.title("Frames | curso")

ventana.geometry("700x700")

#%% Marco Padre
marco_padre = Frame(ventana,width=250,height=250)
marco_padre.config(bg="lightblue",  #Fondo
            bd=4,      #borde
            relief= SUNKEN  #Reliebe --> flat,groove,raised,ridge,solid,sunken
            )
marco_padre.pack(side=BOTTOM,anchor=S,expand=YES,fill=X)



#%% Marco 1
marco = Frame(marco_padre,width=250,height=250)
marco.config(bg="red",  #Fondo
            bd=4,      #borde
            relief= SUNKEN  #Reliebe --> flat,groove,raised,ridge,solid,sunken
            )
marco.pack(side=LEFT,anchor=SW)
marco.pack_propagate(False) #Evita que el marco se contraiga
    #Texto dentro de marco
texto = Label(marco,text = "Texto dentro de marco")
texto.config(bg="red",
            fg="white", #Color fuente
            font=("Arial",10),
            height=10,
            width=15,    #Para poder posicionar un elemento debe de tener dimensiones asignadas
            anchor=CENTER,
            bd=3,
            relief=SOLID
            )
texto.pack(fill=Y,expand=YES)


#%% Marco 2
marco = Frame(marco_padre,width=250,height=250)
marco.config(bg="green",  #Fondo
            bd=4,      #borde
            relief= SUNKEN  #Reliebe --> flat,groove,raised,ridge,solid,sunken
            )
marco.pack(side=RIGHT,anchor=SE)

    #Texto dentro de marco
texto = Label(marco,text = "Texto dentro de marco")
texto.config(bg="blue",
            fg="white", #Color fuente
            font=("Arial",20),
            height=10,
            width=15,    #Para poder posicionar un elemento debe de tener dimensiones asignadas
            anchor=CENTER,
            bd=3,
            relief=SOLID
            )
texto.pack(fill=Y,expand=YES)

ventana.mainloop()
