import Usuarios.usuarios as modelo
import Notas.acciones
import os
class Acciones:

    def registro(self):
        print("Vamos a registrarte")
        nombre = input("Ingrese Nombre: ")
        apellidos = input("Ingrese Apellidos: ")
        email     = input("Ingrese Email: ")
        while True:
            contrasena = input("Ingrese contrasena: ")
            rcontrasena = input("Confirmar contrasena: ")
            if contrasena == rcontrasena:
                break
            else:
                print("No coincide Contraseña. Intente de nuevo")

        usuario = modelo.Usuario(nombre,apellidos,email,contrasena)
        registro = usuario.registrarse()

        if registro[0] >=1:
            print(f"Usuario Registrado con sig info: {registro[1].nombre} {registro[1].apellidos} {registro[1].email} a las {registro[1].fecha}")

        else:
            print("No te has registrado correctamente")
    
    def login(self):
        #try:
            print("Ingresando...")
            correo = input("Ingrese usuario: ")
            contrasena = input("Ingrese contrasena: ")
            usuario = modelo.Usuario('','',correo,contrasena)
            login = usuario.identificarse() #Devuelve consulta  cursor.fetchone()
            if correo == login[3]:
                print (f"Bienvenido {login[1]}, has ingresado")
                self.proximasacciones(login)

        #except TypeError:
            
            #Codigo para ver que clase de errores se muestra
            #print (type(e))             #Tipo de error,Clase
            #print (type(e).__name__)    #Devuelve nombre del error
            #print ("No existe usuario...")
            

    def proximasacciones(self,usuario):
        print("""
        ACCIONES DISPONIBLES:
            - Nueva Nota (crear)
            - Mostrar NOtas (mostrar)
            - Eliminar nota (eliminar)
            - Salir(salir)
        """)
        accion  = input("¿Qué quieres hacer?: ")
        hazEL = Notas.acciones.Acciones() #Objeto de la classe menu de acciones
        if accion =="crear":         
            #print("Vamos a crear")
            hazEL.crear(usuario)
        elif accion == "mostrar":    
            #print("Vamos a mostrar")
            hazEL.mostrar(usuario)
            print("\n")
            self.proximasacciones(usuario)
        elif accion == "eliminar":   
            #print("Vamos a eliminar")
            hazEL.borrar(usuario)
            print("\n")
            self.proximasacciones(usuario)
        elif accion == "salir":      
            exit()
        else:
            os.system('clear')
            print("Su opcion no existe \n")
            self.proximasacciones(usuario)
        return None
