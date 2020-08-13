from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100,verbose_name="Titulo")
    content = RichTextField(verbose_name = "Contenido")
    slug = models.CharField(max_length=150,verbose_name="URL",unique=True) #Unique-->unico y diferente slug --> URL
    order = models.IntegerField(default='0',verbose_name='Orden') #Permite guardar un campo Campo para el orden
    visible = models.BooleanField(verbose_name="Visible")
    create_at =models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    update_at =models.DateTimeField(auto_now=True ,verbose_name="Actualizado")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
    
    def __str__(self):
        return self.title   #Poder imprimir el titulo de cada una de las paginas en el panel
    