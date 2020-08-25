from django.contrib import admin
from  .models import *
# Register your models here.

class  CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at','updated_at')
    list_display = ('name','create_at')
    search_fields = ('name','description')


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields =('user','create_at','updated_at')
    search_fields = ('titulo','user')
    list_display = ('titulo','user','public','create_at')
    list_filter = ('public','user','categories')

    #Metodo para cuando se guardan articulos 
    def save_model(self,request,obj,form,change):  
        if not obj.user_id: #Si no me llega un id de usuario
            obj.user_id = request.user.id   #Le asigno un valor
        obj.save()


admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)