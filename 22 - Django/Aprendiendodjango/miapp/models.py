from django.db import models

# Create your models here.
"""
CLASE META --> Permite modificacion de la clase a nivel administrador
                Los resultados se veran reflejados en el panel de administracion
"""

class Article(models.Model):
    title= models.CharField(max_length=150,verbose_name="Titulo")  #Campo de filtro varchar
    content= models.TextField(verbose_name = "Contenido") #Campo de texto, hasta donde permita guardar
    public= models.BooleanField(verbose_name = "Publico")  #Campo boleano
    imagen= models.ImageField(default='null',verbose_name = "Icono",upload_to='articles')
    create_at= models.DateTimeField(auto_now_add=True, verbose_name= "Creacion")  #Fecha automatica de adición de creacion
    updated_at = models.DateTimeField( auto_now=True, verbose_name = "Modificacion")   #Fecha cada que se use

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-create_at']

    #Mostrar info en el panel de admin, de cada objeto
    def __str__(self):  #Magic methods python
        if self.public:
            publico="(Publicado)"
        else:
            publico="(Privado)"
        return f"{self.title} {publico}"



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_ad = models.DateField() #Guardar fecha manual
    
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']

