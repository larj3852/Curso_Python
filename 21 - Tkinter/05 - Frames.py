from tkinter import *
from PIL import Image, ImageTk

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

#Marco 1
marco = Frame(marco_padre,width=250,height=250)
marco.config(bg="red",  #Fondo
            bd=4,      #borde
            relief= SUNKEN  #Reliebe --> flat,groove,raised,ridge,solid,sunken
            )
marco.pack(side=LEFT,anchor=SW)

#Marco 2
marco = Frame(marco_padre,width=250,height=250)
marco.config(bg="green",  #Fondo
            bd=4,      #borde
            relief= SUNKEN  #Reliebe --> flat,groove,raised,ridge,solid,sunken
            )
marco.pack(side=RIGHT,anchor=SE)


#%%
#Marco Padre
marco_padre = Frame(ventana,width=250,height=250)
marco_padre.config(bg="lightblue",  #Fondo
            bd=4,      #borde
            relief= SUNKEN  #Reliebe --> flat,groove,raised,ridge,solid,sunken
            )
marco_padre.pack(side=TOP,anchor=N,expand=YES,fill=X)


#Marco 3
marco = Frame(marco_padre,width=250,height=250)
marco.config(bg="orange",  #Fondo
            bd=4,      #borde
            relief= SUNKEN  #Reliebe --> flat,groove,raised,ridge,solid,sunken
            )
marco.pack(side=RIGHT,anchor=NW)


#Marco 3
marco = Frame(marco_padre,width=250,height=250)
marco.config(bg="black",  #Fondo
            bd=10,      #borde
            relief= GROOVE  #Reliebe --> flat,groove,raised,ridge,solid,sunken
            )
marco.pack(side=LEFT,anchor=NE)



ventana.mainloop()