from django.contrib import admin
from .models import Article,Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):   #Clase que permite manupular modelos en el panel de adminstracion
    #Mostrar datos de solo lectura
    readonly_fields = ('create_at','updated_at')
    
admin.site.register(Article,ArticleAdmin)   #Paso la clase para mostrar en pantalla admin las modificaciones
admin.site.register(Category)