from django.urls import path
from . import views

urlpatterns = [

    path('articulos/',views.list,name="list_articles"),
    path('categorias/<int:category_id>',views.category,name='list_categories'),
    path('articulo/<int:article_id>',views.article,name='articulo')
]