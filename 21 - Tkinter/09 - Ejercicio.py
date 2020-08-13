"""
REALIZACION DE UNA CALCULADORA CON:
    - Dos campos de texto
    - 4 botones para las operaciones
    - Mostar el resulltado en una alerta
"""

from tkinter import *
from tkinter import messagebox


ventana= Tk()
ventana.title("Ejercisio: Calculadora")
ventana.geometry("400x300")
num1 = StringVar()
num2 = StringVar()
resultado=StringVar()

#Funciones

def convertfloat(numero):       #Evita que se metan otros datos que no sean numeros
    try:
        result= float(numero)
        return result
    except:
        messagebox.showerror("Error","Introduce numeros")

def sumar():
    resultado.set(convertfloat(num1.get())+convertfloat(num2.get()))
    Mostrarresultado()

def restar():
    resultado.set(convertfloat(num1.get())-convertfloat(num2.get()))
    Mostrarresultado()

def multiplicar():
    resultado.set(convertfloat(num1.get())*convertfloat(num2.get()))
    Mostrarresultado()

def dividir():
    resultado.set(convertfloat(num1.get())/convertfloat(num2.get()))
    Mostrarresultado()

def Mostrarresultado():
    messagebox.showinfo("Resultado",f"EL resultado de la operacion es: {resultado.get()}")

#Marco
marco = Frame(ventana,width=300,height=200)
marco.config(bd=5,
            relief=SOLID
            )
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

#Entrada botones
Label(marco,text="Primer Numero").pack()
Entry(marco,textvariable = num1,justify="center").pack()
Label(marco,text="Segundo Numero").pack()
Entry(marco,textvariable = num2,justify="center").pack()

#Operaciones
Button(marco,text="Sumar",command=sumar).pack(side=LEFT,fill=X, expand=YES)
Button(marco,text="Restar",command=restar).pack(side=LEFT,fill=X, expand=YES)
Button(marco,text="Multiplicar",command=multiplicar).pack(side=LEFT,fill=X, expand=YES)
Button(marco,text="Dividir",command=dividir).pack(side=LEFT,fill=X, expand=YES)

ventana.mainloop()