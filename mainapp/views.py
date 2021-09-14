from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {
        'data': 'Inicio de la pagina'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre la pagina',
        'about': 'Esta es la pagina'
    })

def register_page(request):

    if request.user.is_authenticated:
        return redirect('Index')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()

                messages.success(request, 'Te has registrado correctamente. ')

                return redirect('/')

        return render(request, 'users/register.html', {
            'titulo': 'Registro',
            'register_form': register_form
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('Index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Index')
            else:
                messages.warning(request, 'No te has podido registrar')

        return render(request, 'users/login.html', {
            'titulo': 'Login',
        })

def logout_user(request):
    logout(request)
    return redirect('login')