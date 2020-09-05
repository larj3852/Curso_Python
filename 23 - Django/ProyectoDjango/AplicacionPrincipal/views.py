from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from .forms import  RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,'main/index.html',{'title':'Inicio'})

def about(request):
    return render (request,'main/about.html')

def registerpage(request):
    """
    Registro del usuario por el Metodo POST, en caso que no haya en el post, se salta el if
    se creará un registro nuevo.
    En caso que si haya registro, se validda, y se registra, y redirige a inicio
    """
    #Comprobando si ya hay una autenticacion
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form = RegisterForm()
    #Creacion de formulario de gesitro de usuarioa
    #register_form = UserCreationForm()    
    register_form = RegisterForm()
    if request.method == 'POST':
        #Pasar todos los campos extraidos de la request.POST
        register_form = RegisterForm(request.POST)

        #Comprobar si el registro es valido
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Te has registrado correctamente')
            return redirect('inicio')

    return render(request,'users/register.html',{'title':'Registro',
                                                'register_form':register_form})

def login_page(request):

    #Comprobando si ya hay una autenticacion
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Autenticacion
        user = authenticate(request,username=username,password=password)
        #Si user no es invalido
        if user is not None:
            #Logeo
            login(request,user)
            return redirect('inicio')
        else:
            messages.warning(request,"No te has identificado correctamente")

    return render(request,'users/login.html',{'title':'Indetificacion'})

def logout_user(request):
    logout(request)
    return redirect('login')