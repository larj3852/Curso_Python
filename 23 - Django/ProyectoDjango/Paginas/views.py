from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def pages(request,slug):
    #Realizacion de consulta
    page = Page.objects.get(slug=slug)
    return render(request,'pages/page.html',{'page':page})

#USER Lara pwd lara