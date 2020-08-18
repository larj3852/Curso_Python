from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import  User

# Create your models here.
class  Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nombre")
    description = models.CharField(max_length=255,verbose_name="Descripcion")
    create_at= models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated_at= models.DateTimeField(auto_now=True,verbose_name="Creado")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self): #Cuando imprima un objeto de este tipo me devuelva su nombre
        return self.name
    
class Article(models.Model):
    titulo = models.CharField(max_length=200,verbose_name="Titulo")
    contenido = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Imagen",upload_to="articles")
    public = models.BooleanField(verbose_name="Publico")
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False) #Relación con un foreign Key
    categories = models.ManyToManyField(Category, verbose_name="Categorias",blank=True,
                                        related_name="articles")  #null='True'
    #Relacion con muchas categorias
    create_at= models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    updated_at= models.DateTimeField(auto_now=True,verbose_name="Creado")
    

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-create_at']    #Orden

    #¿Como mostrar en el panel de adminstracion?
    def __str__(self):
        return f"{self.titulo}"