from blog.models import Category,Article


#Sacar las categorias
def get_categories(request):

    #Filtrar categorias que tienen articulos sacando sus ids
    ids_categories_in_use = Article.objects.filter(public=True).values_list('categories',flat=True)
    categories = Category.objects.filter(id__in=ids_categories_in_use).values_list('id','name')
    return({
        'categories':categories,
        'ids':ids_categories_in_use
    })