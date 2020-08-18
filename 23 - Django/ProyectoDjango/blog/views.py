from django.shortcuts import render, redirect, get_object_or_404
from blog.models import  Article,Category
# Create your views here.
def list(request):
    #Creacion de consulta a la DB
    articles = Article.objects.all()
    return render(request,'articles/list.html',{
        'title':'Articulos',
        'articulos':articles
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