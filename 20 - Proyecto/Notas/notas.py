import Usuarios.conexion as conexion
connect = conexion.conectar()
database = connect[0]
cursor   = connect[1]

class Nota:
    def __init__(self,usuario_id, titulo="", descripcion=""):   #Inicio de la nota
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    
    def guardar(self):
        
        sql = "INSERT INTO notas VALUES(null,%s,%s,%s,NOW())" #id_usuario,titulo,descripcion
                                                            #NOW()-->funcion sql
        nota = (self.usuario_id,self.titulo,self.descripcion)
        cursor.execute(sql,nota)
        database.commit()
        return [cursor.rowcount,self]    #Comprobar cambios
    
    def listar(self):
        sql= f"SELECT * FROM notas WHERE usuario_id= {self.usuario_id}"
        cursor.execute(sql)
        database.commit()
        resultado = cursor.fetchall()  #Almacenamiento de todos los datos de la consulta
        return resultado

    def eliminar(self,titulo):
        sql = f"DELETE FROM notas WHERE usuario_id={self.usuario_id} AND titulo LIKE '{titulo}'"
        # LIKE --> cuando el titulo esté contenido dentro del titulo
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount,self]
        
        