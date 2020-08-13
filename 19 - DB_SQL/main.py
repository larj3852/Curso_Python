

#%% Conexion
import mysql.connector
Database = mysql.connector.connect(host =  "localhost",
                                    user = "root",
                                    password = "",
                                    database="master_python")

#config = {"host":"localhost","user":"root","passwd":''}
#Database = mysql.connector.connect(**config)
#La conexion ha sido correcta 
print(Database)

cursor = Database.cursor(buffered=True) #-->Consultas ilimitadass
#%% Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

#%% CREAR TABLA
cursor  .execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vihiculo PRIMARY KEY(id)
)
""")
cursor.execute("SHOW TABLES")
for tabla in cursor:
    print(tabla)

#%% INSERTAR DATOS
cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Astra',18500)")
Database.commit()
#Database.close()

#%%     INSERTAR DATOS MASIVOS
coches = [
            ('Seat','Ibiza',5000),
            ('Renault','Clio',1500),
            ('Citroen','Saxo',20000),
            ('Mercedes','Clase C',35000)
            ]
cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)",coches)
Database.commit()
# %%   CONSULTA
cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()  #--> Devuelve un tuple

print("---------COCHES-----------")
for coche in result:
    print(coche)


# %%    BORRAR Y ACTUALIZAR REGISTROS
cursor.execute("DELETE FROM vehiculos WHERE marca  = 'Mercedes' ")
Database.commit()

print(cursor.rowcount,"Borrados!!") # rowcount --> Muestra numero de borrados

# %% ACTUALIZAR
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")
Database.commit()

print(cursor.rowcount,"Actualizados!")
# %%
