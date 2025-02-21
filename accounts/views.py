from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, LoginForm

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            if not User.objects.filter(username=email).exists():
                messages.error(request, "E-mail inexistente")
                return render(request, 'login.html', {'form': form})

            user = authenticate(request, username=email, password=senha)
            if user is not None:
                django_login(request, user)
                return redirect('menu')
            else:
                if senha.strip() == '':
                    messages.error(request, "Senha não pode ser vazia.")
                else:
                    messages.error(request, "Senha inválida")
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, "E-mail inválido")
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']


            # Verificar se o e-mail já está cadastrado
            if User.objects.filter(email=email).exists():
                form.add_error('email', "E-mail já cadastrado.")
                return render(request, 'signup.html', {'form': form})

            # Criar usuário
            user = User.objects.create_user(
                username=email,
                email=email,
                password=senha,
                first_name=nome
            )
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def menu(request):
    return render(request, 'menu.html')