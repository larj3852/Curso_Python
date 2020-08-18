from django.shortcuts import render
from .models import Page

# Create your views here.
def pages(request,slug):
    #Realizacion de consulta
    page = Page.objects.get(slug=slug)
    return render(request,'pages/page.html',{'page':page})

#USER Lara pwd lara