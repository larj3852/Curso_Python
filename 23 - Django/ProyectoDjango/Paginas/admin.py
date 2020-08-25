from django.contrib import admin
from .models import Page
# Register your models here.

#Agregar modelos al panel de adminstracion

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ("create_at","update_at") #Mostrar readonly dields
    search_fields = ('title','content') #Busqueda por campos
    list_filter =   ('visible',) #Filtrado de articulos
     

admin.site.register(Page,PageAdmin)

admin.site.site_header = "Proyecto Con Django"
admin.site.index_title = "Panel de gestion"
    