from django.shortcuts import render, redirect
#Agrega plantillas en este caso para  registrarse
#from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html',{
        'title':'Inicio',
        'content':'.:: Bienvenido a mi pagina de inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title':'Acerca De',
        'content':'.:: Somo un equipo de desarrollo de SW Multiplataforma con Django ::.'
    })

def mision(request):
    return render(request, 'mainapp/mision.html',{
        'title':'Mision',
    })

def vision(request):
    return render(request, 'mainapp/vision.html',{
        'title':'Vision',
    })
################################################################
def registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form=RegisterForm()
        
        if request.method == "POST":
            register_form=RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request,"¡¡¡Registro exitoso!!!")
                return redirect('inicio')
    
        return render(request, 'users/registro.html',{
            'title':'Registro',
            'register_form':register_form
        })

def inicio_secion(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"¡Bienvenido al inicio de seción!")
                return redirect('inicio')
            else:
                messages.warning(request,"Credeciales incorrectas")


        return render(request, 'users/inicio_secion.html',{
            'title':'Inicio de sesión',
            'content':'Formulario de inicio de seción'
        })
    
def logout_user(request):
    logout(request)
    return redirect('inicio')
################################################################
# Redirige a la URL deseada, por ejemplo, la página de inicio con error 404 1er forma
def redireccion_404(request, exception):
    return redirect('inicio')

# Redirige a la URL deseada, por ejemplo, la página de inicio con error 404 2da forma
def error404_2(request, exception):
    return render(request,'mainapp/404.html')

#Registro
#Solo diga formulario de registro
#Inicio de sesión
#Solo diga formulario de inicio de secion