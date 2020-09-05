from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<int:apellidos>')
def informacion(nombre = '',apellidos = ''): #None
    texto = 'Pepa pig'
    if nombre!='' and apellidos!='':
        texto = f"""<h1>pagina de informacion</h1>
                    <h2>{nombre} {apellidos}</h2>"""
    return render_template('informacion.html',texto=texto)

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):
    if redireccion is not None:
        #Redireccionamiento
        return redirect(url_for('lenguajes'))
    else:
        return render_template('contacto.html')

@app.route('/lenguajes')
def lenguajes():
        return render_template('lenguajes.html')


if __name__ == '__main__':
    app.run(debug=True)