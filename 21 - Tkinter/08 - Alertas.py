from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacaralerta():
    MessageBox.showinfo("Alerta","Soy una alerta")
    
Button(ventana,text="Alerta!",command=sacaralerta).pack()

def salir(nombre):
    resultado=MessageBox.askquestion("Salir","¿Quieres continuar con la aplicacion?")
    if resultado!="yes":
        MessageBox.showinfo("Ciao!",f"Adios {nombre}")
        ventana.destroy()

#Cuando se quieren pasar parametros de una función, se utiliza la función lambda
Button(ventana,text="salir",command= lambda: salir("Jesus")).pack()

ventana.mainloop()