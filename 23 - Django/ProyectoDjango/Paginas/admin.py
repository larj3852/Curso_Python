from django.contrib import admin
from .models import Page
# Register your models here.

#Agregar modelos al panel de adminstracion
admin.site.register(Page)

admin.site.site_header = "Proyecto Con Django"
admin.site.index_title = "Panel de gestion"
    