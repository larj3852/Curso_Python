from django.shortcuts import render, redirect, get_object_or_404
from blog.models import  Article,Category
from django.core.paginator import Paginator
# Create your views here.
def list(request):
    articles = Article.objects.all()            #Creacion de consulta a la DB
    """ Creacion de paginaciones"""
    paginator = Paginator(articles,2)           #Creacion de la paginación
    page = request.GET.get('page')              #Recpge el numero de la pagina por la URL
    page_articles = paginator.get_page(page)    #Crea una variable de todos los articulos paginados

    return render(request,'articles/list.html',{
        'title':'Articulos',
        'articulos':page_articles   #Se pasa la variable con los articulos ya paginados
    })


def BorrarArticulo(request,id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()
    return redirect("articles/list.html")

def category(request,category_id):
    #category = Category.objects.get(id=category_id)

    #Error 404
    category = get_object_or_404(Category,id=category_id)
    articles = Article.objects.filter(categories=category_id)
    return render(request,'categories/category.html',{'category':category,
                                                        'articulos':articles})

def article(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
    return render(request,'articles/detail.html',{'articulo':article})