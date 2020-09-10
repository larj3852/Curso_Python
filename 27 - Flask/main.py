from flask import Flask, redirect, url_for, render_template, request, flash
from datetime import datetime
from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'

#Conexion MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_UNIX_SOCKET'] = '/opt/lampp/var/mysql/mysql.sock'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Proyecto_Flask'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)
#Context processors
@app.context_processor
def date_now():
    return {'now':datetime.utcnow}

#Main page
@app.route('/')
def index():
    return render_template('index.html')

#Information page
@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<int:apellidos>')
def informacion(nombre = '',apellidos = ''): #None
    texto = 'Pepa pig'
    if nombre!='' and apellidos!='':
        texto = f"""<h1>pagina de informacion</h1>
                    <h2>{nombre} {apellidos}</h2>"""
    return render_template('informacion.html',texto=texto)

#Contacto page
@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):
    if redireccion is not None:
        #Redireccionamiento
        return redirect(url_for('lenguajes'))
    else:
        return render_template('contacto.html')

#Languages page
@app.route('/lenguajes')
def lenguajes():
        return render_template('lenguajes.html')

#insertar coche
@app.route('/insertar-coche', methods=['GET','POST'])
def insertar_coche():
    if request.method == 'POST':

        marca  = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
        #Conexion con la bd
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL,%s,%s,%s,%s)",(marca,modelo,precio,ciudad))
        cursor.connection.commit()
        cursor.close()
        flash('¡Has creado un nuevo coche!')
        return redirect(url_for('index'))
        
    return render_template('crear_coche.html')

"""Vista Listado de coches """
@app.route('/coches')
def coches():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches ORDER BY id DESC")
    coches = cursor.fetchall()
    cursor.close()
    return render_template('coches.html',coches=coches)

"""Vista  Detallada Cohes"""
@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s",(coche_id))   #En una tupla
    coche = cursor.fetchall()
    cursor.close()
    return render_template('coche.html',coche=coche[0]) 
    #Indice 0 , porque está en una tupla de tuplas

"""ELiminar coche"""
@app.route('/eliminar_coche/<coche_id>')
def eliminar_coche(coche_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM coches WHERE id = %s",(coche_id))   #En una tupla
    cursor.connection.commit()
    cursor.close()
    flash('El coche ha sido eliminado!!')
    return redirect(url_for('coches'))
    #Indice 0 , porque está en una tupla de tuplas


"""Editar coche"""

@app.route('/editar_coche/<coche_id>', methods=['GET','POST'])
def editar_coche(coche_id):
    if request.method == 'POST':
        marca  = request.form['marca']
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']
        #Conexion con la bd
        cursor = mysql.connection.cursor()
        cursor.execute("""UPDATE coches
                        SET marca = %s, modelo = %s, precio = %s, ciudad = %s        
                        WHERE id=%s
                        """ 
                        ,(marca,modelo,precio,ciudad,coche_id))
        cursor.connection.commit()
        cursor.close()
        flash(f'¡Has Editado el coche {marca} correctamente!')
        return redirect(url_for('index'))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s",(coche_id))   #En una tupla
    coche = cursor.fetchall()
    cursor.close()
    return render_template('editar_coche.html',coche=coche[0]) 
    #Indice 0 , porque está en una tupla de tuplas


#Start app
if __name__ == '__main__':
    app.run(debug=True)