from Paginas.models import Page

def get_pages (request):
    #Si pasamos todos los valores, será mas pesado para el servidor, es mejo
    #pasar los que se van a ocupar
    pages = Page.objects.filter(visible=True).order_by("order").values_list('id','title','slug') #flat=True #Flat -> Texto plano
    #pages = Page.objects.all

    return {'pages':pages}