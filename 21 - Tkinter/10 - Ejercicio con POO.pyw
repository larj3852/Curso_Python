import tkinter
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.ventana= tkinter.Tk()
        self.ventana.geometry("500x500")
        self.num1 = tkinter.StringVar()
        self.num2 = tkinter.StringVar()
        self.resultado=tkinter.StringVar()
        #Marco
        marco = tkinter.Frame(self.ventana,width=300,height=200)
        marco.config(bd=5,
                    relief=tkinter.SOLID
                    )
        marco.pack(side=tkinter.TOP, anchor=tkinter.CENTER)
        marco.pack_propagate(False)

        #Entrada botones
        tkinter.Label(marco,text="Primer Numero").pack()
        tkinter.Entry(marco,textvariable = self.num1,justify="center").pack()
        tkinter.Label(marco,text="Segundo Numero").pack()
        tkinter.Entry(marco,textvariable = self.num2,justify="center").pack()

        #Operaciones
        tkinter.Button(marco,text="Sumar",command=self.sumar).pack(side=tkinter.LEFT,fill=tkinter.X, expand=tkinter.YES)
        tkinter.Button(marco,text="Restar",command=self.restar).pack(side=tkinter.LEFT,fill=tkinter.X, expand=tkinter.YES)
        tkinter.Button(marco,text="Multiplicar",command=self.multiplicar).pack(side=tkinter.LEFT,fill=tkinter.X, expand=tkinter.YES)
        tkinter.Button(marco,text="Dividir",command=self.dividir).pack(side=tkinter.LEFT,fill=tkinter.X, expand=tkinter.YES)


    def abrirapp(self):
        self.ventana.mainloop()

#%% Funciones Operacionales

    def convertfloat(self,numero):       #Evita que se metan otros datos que no sean numeros
        try:
            result= float(numero)
            return result
        except:
            messagebox.showerror("Error","Introduce numeros")

    def sumar(self):
        self.resultado.set(self.convertfloat(self.num1.get())+self.convertfloat(self.num2.get()))
        self.Mostrarresultado()

    def restar(self):
        self.resultado.set(self.convertfloat(self.num1.get())-self.convertfloat(self.num2.get()))
        self.Mostrarresultado()

    def multiplicar(self):
        self.resultado.set(self.convertfloat(self.num1.get())*self.convertfloat(self.num2.get()))
        self.Mostrarresultado()

    def dividir(self):
        self.resultado.set(self.convertfloat(self.num1.get())/self.convertfloat(self.num2.get()))
        self.Mostrarresultado()

    def Mostrarresultado(self):
        messagebox.showinfo("Resultado",f"EL resultado de la operacion es: {self.resultado.get()}")



#Inicio Programa
calculadora=Calculadora()
calculadora.abrirapp()