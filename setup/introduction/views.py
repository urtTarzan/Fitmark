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
def logout_view(request):
    logout(request)
    return redirect('introduction_home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            context = {
                "error": "Usuário ou senha incorretos.",
                "username_value": username,
                "open_login_modal": True  # <--- aqui diz pro template abrir o modal
            }
            return render(request, "introduction/home.html", context)


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        context = {"username": username, "email": email}

        # Senhas não conferem
        if password1 != password2:
            context["error"] = "As senhas não conferem."
            return render(request, "register.html", context)

        # Usuário já existe
        if User.objects.filter(username=username).exists():
            context["error"] = "Conta já existente."
            return render(request, "register.html", context)

        # Criar usuário
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Autenticar e redirecionar para home
        login(request, user)
        return redirect("home")

    return render(request, "register.html")

def erro_login(request):
    return render(request, 'introduction/error/login_error.html')