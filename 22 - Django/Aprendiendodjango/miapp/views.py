from django.shortcuts import render , HttpResponse, redirect
from django.db import models
from miapp.models import Article
from miapp.forms import FormArticle
from django.contrib import messages

#layout para navegacion entre rutas
layout = """
<h1>    Sitio web con Django </h1>
<hr>
<ul>
        <li>
            <a href="/inicio"> Inicio</a> </li>
        <li>
            <a href="/hola-mundo"> Hola mundo</a> </li>
        <li>
            <a href="/pagina-prueba"> Prueba</a> </li>
        <li>
            <a href="/contacto"> Contacto</a> </li>
</lu>
</r>
"""



# Create your views here.

def index(request):
    """ EJEMPLO DE PASAR VARIABLE CON RESULT HTML AÑOS DE 2020-2050
    
    html=''
    <h1> Inicio </h1>
    <p>Años pares    hasta el 2050: </p>
    <ul>
    </r>

    year=2021
    while year<=2050:
        if year%2==0:
            html += f"<li>{str(year)}</li>"

        year+=1
        

    html+="</u>"
    """
    lenguajes = ['Js','Python','sql','Java','C++']
    years= 2021
    hasta=range(years,2051)
    return render(request,'index.html',{'mi_variable':'Esta es la variable desde la vista.py',
                                        'titulo':'Este es el titulo en vista.py',
                                        'nombre':'Pedro Picapiedra',
                                        'lenguajes':lenguajes,
                                        'years': hasta})
   

def hola_mundo(request):
    return render(request,"holamundo.html")

def pagina(request,redirigir=0):

    if redirigir==1:
        return redirect("contacto",nombre="Pedro",apellidos="Picapiedra")
        #Hacerlo de esta manera, es una forma más limpia, ya que si se cambiaran
        #El nombre de las rutas, la función de guía por el nombre puesto en el PATH
        #path(name="...")
    return render(request,'pagina.html')

def contacto (request,nombre="",apellidos=""):
    return HttpResponse(layout+f"<h2>Ruta para contacto {nombre} {apellidos}</h2>")

#%%Django + SQL 

def crear_articulo(request,title,content,public):
    #Se crea el objeto
    articulo = Article( 
            title = title,
            content = content,
            public = public
    )
    articulo.save() #Hay otros métoodos como create
    return HttpResponse(f"<h3>Articulo Creado: {articulo.title} {articulo.content} {articulo.public}</h3>")


def Articulo(request):
    try:
        articulo = Article.objects.get(id=30)  #id,pk Esto es como una consulta, por lo cual se debe par un parametro de identificacion
        return HttpResponse(f"Articulo<br>{articulo.id}.{articulo.title}")
        
    except:
        response = "<h1>Articulo No Encontrado</h1>"
        return HttpResponse(response)

def EditarArticulo(request,id):

    articulo= Article.objects.get(pk=id)
    articulo.title = "Batman"
    articulo.content = "Es mejor que superman"
    articulo.public =  True

    articulo.save()
    return HttpResponse(f"Articulo: {articulo.title} editado!")

#Obtener todos los elementos de la tabla
def Articulos(request):
    articulos=Article.objects.all()
    articulos=Article.objects.filter(public=True).order_by("-id")
    #articulos=Article.objects.order_by('-id')[2:6] #(-title') /Limit by  
    #Se pueden limitar el num de articulos amostrar
    return render(request,'articulos.html',{'articulos':articulos})

def BorrarArticulo(request,id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()
    return redirect("articulos")


#%% FORMULARIOS 

def save_article(request):
    if request.method == 'POST':
        title   = request.POST['title']
        content = request.POST['content']
        public  = request.POST['public']
        #Se crea el objeto
        articulo = Article( 
                title = title,
                content = content,
                public = public
        )
        articulo.save() #Hay otros métoodos como create
        return HttpResponse(f"<h3>Articulo Creado: {articulo.title} {articulo.content} {articulo.public}</h3>")
    
    else:
        return HttpResponse("<H2>No se ha podido crear el artículo</H2>")



def create_article(request):
    return render(request,'create_article.html')

#%% CREACION FORMULARIOS MEDIANTE DJANGO

def create_full_article(request):
    
    #Si deslde el formularios nos envia datos
    if request.method == 'POST':
        formulario = FormArticle(request.POST)  #Limpieza y validación de datos Django

        if formulario.is_valid(): #Validacion del formulario
            data_form= formulario.cleaned_data  #Datos limpios que llegan

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article( 
                title = title,
                content = content,
                public = public
            )

            articulo.save()
            # CREACION DE MENSAJE MEDIANTE SESION FLASH
            #Creacion de sesion
            messages.success(request,f'Has creado correctamente el articulo {articulo.id}')
            return redirect('articulos')
            #return HttpResponse(f"{articulo.title} | {articulo.content} | {str(articulo.public)}")
    else:
        formulario = FormArticle()

    return render(request,'create_full_article.html',{'form':formulario})