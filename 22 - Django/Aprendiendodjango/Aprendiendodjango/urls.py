"""Aprendiendodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Impotartacion miapp con vistas
from miapp import views
from django.conf import settings

#CAMBIAR TITULO DEL PANEL DE ADNIMISTRACION

admin.site.site_header = "Pagina Web del Pato"
admin.site.index_title = "Gestion Web"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path("inicio/",views.index,name="inicio"),
    path('hola-mundo/',views.hola_mundo,name="HolaMundo"),
    #Ejemplo Redirecciones
    path('pagina-prueba/',views.pagina,name="pagina-prueba"),
    path('pagina-prueba/<int:redirigir>',views.pagina,name="pagina-prueba"),
    #Parametros opcionales: 3 casos
    path('contacto/',views.contacto,name="contacto"),
    path('contacto/<str:nombre>',views.contacto,name="contacto"),
    path('contacto/<str:nombre>/<str:apellidos>',views.contacto,name="contacto"),
    #Manejo con base de datos sqlite
    path('crear-articulo/<str:title>/<str:content>/<str:public>',views.crear_articulo,name="crear_articulo"),
    path('articulo/',views.Articulo,name="articulo"),
    path('editar-articulo/<int:id>',views.EditarArticulo,name='editararticulo'),
    path('articulos/',views.Articulos,name='articulos'),
    path('borrar-articulo/<int:id>',views.BorrarArticulo,name='borrar'),
    path('save-article/',views.save_article,name='save'),
    path('create-article/',views.create_article,name='create'),
    path('create-full-article/',views.create_full_article,name='createfull')
]

    #Configuracion para cargar imagenes
if settings.DEBUG:  #Verfifciar si estamos en modo DEBUG (Local) o PRODUCCION
    from django.conf.urls.static import static 
        #Solamente se importará si es encesario
        #static --> permitira cargar en url a un fichero statico que pueda leer el framework

                #SE CARGA EL DIRECTORIO A LLEER
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)