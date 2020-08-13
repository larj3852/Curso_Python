import Notas.notas
class Acciones:

    def crear(self,usuario):    #Usuario --> Se pasan todos los argumentos de la consulta
        print(f"\n{usuario[1]} creando nueva nota")

        titulo = input("Ingresa el titulo de tu nota: ")
        descripcion = input("Empieza a escribir: ")
        nota = Notas.notas.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0]>=1:
            print(f"\nSe ha guardado la nota '{titulo}' ")
        else:
            print(f"{usuario[1]}, no se ha guardado la nota :(")
    
    def mostrar(self,usuario):
        print(f"\nEstas son las notas de {usuario[1]}: \n")
        nota = Notas.notas.Nota(usuario[0],"","") #id usuario ,titulo n nota, descripcion
        notas = nota.listar()
        if notass:
            for nota in notas:
                print("------------------------------------")
                print(f"Titulo: {nota[2]}")
                print(f"Fecha creacion: {nota[4]}")
                print(f"{nota[3]}")
                print("------------------------------------\n")
        else:
            print("\n NO HAY NOTAS")
    
    def borrar(self,usuario):
        print(f"\n {usuario[1]}, vamos a borrar notas:\n")
        titulo = input("Introduce el titulo de la nota que quieras borrar: ")
        nota = Notas.notas.Nota(usuario[0],titulo,"")
        eliminar = nota.eliminar(titulo)

        if eliminar[0]>=1:
            print("\n¡Tu nota fue borrada con éxito!")
        else:
            print("\n No se ha borrado la nota, intenta de nuevo :(")
            


    