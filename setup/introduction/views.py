from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'introduction/home.html')

def parceria(request):
    return render(request, 'introduction/parceria.html')

def sobre(request):
    return render(request, 'introduction/sobre.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')  # ou a página que você quiser
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return redirect('home')  # recarrega a página base (com modal)
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # validações básicas
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('home')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return redirect('home')

        # cria o usuário
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('home')

    return redirect('home')