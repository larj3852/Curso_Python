
import datetime
import hashlib
import Usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self,nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrarse(self):
        self.fecha = datetime.datetime.now()
        #Cifrar contrasena
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) #update acepta argumentos Byte


        sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"   #Consulta --> Id,nombre, apellido,correo,contrasena
        #La contrasena se almacena en valor hexadecimal
        usuario = (self.nombre,self.apellidos,self.email,cifrado.hexdigest(),self.fecha)
        try:
            cursor.execute(sql,usuario)
            database.commit()  #Guardado
            return [cursor.rowcount,self]   #Numero de cambios, objeto con valores

        except:                             #Detecta el error de correos duplicados
            return  [0,self]

    def identificarse(self):
        #Consulta
        sql = "SELECT * FROM usuarios WHERE email =%s AND password =  %s"

        #Cifrar Contrasena
        cifrado = hashlib.sha256()  #NOTA: El tipo de cifrado debe concordar
        cifrado.update(self.password.encode('utf8'))
        usuario = (self.email, cifrado.hexdigest())
        cursor.execute(sql,usuario)
        result = cursor.fetchone()
        return result

