"""
Crear un programa que:
    - Una ventana
    - Tamaño fijo
    - Tamaña no redimencionable
    - Un menu (Inicio, Añadir, Informacion,Salirs)
    - Diferentes pantallas accedidas a travez del menu
    - Formulario de añadir productos
    - Guardar datos temporalmente
    - Mostrar datos listados en la pantalla principal home
"""

from tkinter import *
from tkinter import ttk

#Definicion de ventana
ventana = Tk()
#ventana.geometry("400x400")
ventana.minsize(500,500)
ventana.resizable(0,0)
ventana.title("Ejercicio 2")




def casa():
    anadir_lable.grid_remove()
    info_lable.grid_remove()
    add_frame.grid_remove()
    #Montar pantañla
    home_lable.config(fg="white",
                        bg="black",
                        font=("calibri",20),
                        padx=100,
                        pady=10
                        )
    home_lable.grid(row=0,column=0,columnspan=2)

    #Listar productos
    productos_tabla.grid(row=1,column=0,columnspan=2)
    """
    for producto in productos:
        if len(producto)==3:    #COmprobar que todos los campos estan llenos
            producto.append("Anadido")  #Cuando pasa pro segunda vez, detecta 4 campon en lugar de 3, y no repite el proucto
            Label(productos_box,text=producto[0]).grid()
            Label(productos_box,text=producto[1]).grid()
            Label(productos_box,text=producto[2]).grid()
            Label(productos_box,text="--------------------").grid()
    """
    for producto in productos:
        if len(producto)==3:    #COmprobar que todos los campos estan llenos
            producto.append("Anadido")  #Cuando pasa pro segunda vez, detecta 4 campon en lugar de 3, y no repite el proucto
            productos_tabla.insert('',0,text=producto[0],values=(producto[1]))

def anadir():
    info_lable.grid_remove()
    home_lable.grid_remove()
    productos_box.grid_remove()
    productos_tabla.grid_remove()
    anadir_lable.config(fg="white",
                        bg="black",
                        font=("calibri",20),
                        padx=130,
                        pady=10
                        )
    anadir_lable.grid(row=0,column=0, columnspan=2,sticky=NW)

    #Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1,column=0,padx=5,pady=5)
    add_name_entry.grid(row=1,column=1,padx=5,pady=5)
    
    add_price_label.grid(row=2,column=0,padx=5,pady=5)
    add_price_entry.grid(row=2,column=1,padx=5,pady=5)

    add_description_label.grid(row=3,column=0,padx=5,pady=5)
    add_description_entry.grid(row=3,column=1,padx=5,pady=5)
    add_description_entry.config(width = 30,
                                height = 5,
                                padx=15,
                                pady=15
                                )

    add_separator= Label(ventana,text="")
    add_separator.grid(row=4)
    add_Boton.config(padx=15,
                    bg= "black",
                    fg="white")

    add_Boton.grid(row=5,column=1,sticky=N)


def info():
    home_lable.grid_remove()
    anadir_lable.grid_remove()
    add_frame.grid_remove()
    productos_box.grid_remove()
    productos_tabla.grid_remove()
    
    info_lable.config(fg="white",
                        bg="black",
                        font=("calibri",20),
                        padx=100,
                        pady=10
                        )
    info_lable.grid(row=0,column=0)
    #Informacion pagina
    Label(ventana,text="Creado por Jesus Lara").grid(row=1,column=0)
    Label(ventana,text="Version 1.0").grid(row=2,column=0)
    Label(ventana,text="Año 2020").grid(row=3,column=0)

def add_productos():
    productos.append(
        [namedata.get(),
        pricedata.get(),
        add_description_entry.get("1.0","end-1c")
        ]
    )
    namedata.set("")
    pricedata.set("")
    add_description_entry.delete("1.0",END)
    
    #print(productos)
    casa() #Regresar a casa

#VARIABLES IMPORTANTES
namedata=StringVar()
pricedata=StringVar()
productos= []

#DEFINICION ENCABEZADO Diferentes pantalla
home_lable = Label(ventana,text="Pagina Home")
anadir_lable = Label(ventana,text="Añadir",justify="center")
info_lable = Label(ventana,text="Acerca de...")

#DEFINICION CAMPOS FORMULARIO
add_frame = Frame(ventana,width=120,height = 80)


add_name_label  =  Label(add_frame,text= "Nombre del producto: ")
add_name_entry  =  Entry(add_frame, textvariable = namedata)

add_price_label =  Label(add_frame,text="Precio del producto: ")
add_price_entry =  Entry(add_frame, textvariable = pricedata)

add_description_label = Label (add_frame,text = "Descripcion: ")
add_description_entry = Text(add_frame)

add_Boton = Button(add_frame,text="Añadir",command=add_productos) 

#CAJA DE PRODUCTOS
productos_box = Frame(ventana,width=300)
Label(productos_box).grid(row=0)
productos_tabla = ttk.Treeview(height=12, columns=2)
productos_tabla.grid(row=1,column=0,columnspan=2)
productos_tabla.heading("#0",text="PRODUCTO",anchor=W)#Emcabezado
productos_tabla.heading("#1",text="PRECIO",anchor=W)#Emcabezado



casa()  #Cargar pantalla inicio
#Menu superior
menusuperior=Menu(ventana)
menusuperior.add_command(label="Inicio",command=casa)
menusuperior.add_command(label="Añadir",command=anadir)
menusuperior.add_command(label="Informacion",command=info)
menusuperior.add_command(label="Salir",command=ventana.quit)

#Cargar menu
ventana.config(menu=menusuperior)

#Cargar ventana
ventana.mainloop()