#%% Importar modulo
import sqlite3
#Conexion
conexion = sqlite3.connect('pruebas.db')

#Crear cursor --> Permitirá realizar las consultas
cursor = conexion.cursor()
#%%
#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "titulo VARCHAR(255),"+
                "descripcion text,"+    
                "precio int(255)"
                ")")

#Insertar datos
    #   *Como el id es autoincremental, se poner null conmo atributo
conexion.execute("INSERT INTO productos VALUES(null,'Primer Producto','descripcion del producto',550)")
#GUARDAR CAMBIOS
conexion.commit()

#%% LECTURA --> Listar los datos
cursor.execute("SELECT * FROM productos;")  # *-->significa que todas las columnas
productos = cursor.fetchall() #Devuelve una tupla
print(productos)

for producto in productos:
    print("\n",producto)
    print("ID: ",producto[0])
    print("Titulo:",producto[1])
    print("Descripcion:",producto[2])
    print("Precio:",producto[3])
#%%
#SACAR PRIMER PRODUCTO
cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

#%% BORAR REGISTROS
cursor.execute("DELETE FROM productos") #--> Borrar todo

#%% CREAR REGISTROS DE GOLPE
productos = [("Laptop","PC",1232),
             ("Movil","Touch",123),
             ("Placa Base","Buena placa",80),
             ("Tablet 15","BUena tablet",300)
            ]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conexion.commit() #Guardarndo cambios

#%%CONSULTA SELECTIVA EJEMPLO:Productos >= 100
cursor.execute("SELECT * FROM productos WHERE precio>=100;")
productos = cursor.fetchall()
for producto in productos:
    print("\n",producto)

#%% ACTUALIZACIÓN DE VALOR 
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")
# %% CERRAR CONEXION --> Si no se cierra conexión el fichero se quedara habierto sin guardar los cambios
conexion.close()





# %%
