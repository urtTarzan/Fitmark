from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
# Create your views here.

def home_introduction(request):
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
                "error_login": "Usuário ou senha incorretos.",
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
        user = authenticate(request, username=username,)

        # Contexto base — mantém nome, e-mail e senha já digitados
        context = {
            "username_value": username,
            "email_value": email,
            "password_1": password1,
            "open_register_modal": True
        }

        # 1️⃣ Senhas não conferem
        if password1 != password2:
            context["error_register"] = "As senhas não conferem."
            return render(request, "introduction/home.html", context)

        # 2️⃣ E-mail inválido
        try:
            validate_email(email)
        except ValidationError:
            context["error_register"] = "E-mail inválido. Insira um e-mail completo (ex: nome@dominio.com)."
            return render(request, "introduction/home.html", context)

        # 3️⃣ Nome de usuário inválido
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            context["error_register"] = "O nome de usuário só pode conter letras, números e _."
            return render(request, "introduction/home.html", context)

        # 4️⃣ Validação de senha forte
        if len(password1) < 8:
            context["error_register"] = "A senha deve ter pelo menos 8 caracteres."
            return render(request, "introduction/home.html", context)

        if not re.search(r"[A-Z]", password1):
            context["error_register"] = "A senha deve conter pelo menos uma letra maiúscula."
            return render(request, "introduction/home.html", context)

        if not re.search(r"[a-z]", password1):
            context["error_register"] = "A senha deve conter pelo menos uma letra minúscula."
            return render(request, "introduction/home.html", context)

        if not re.search(r"\d", password1):
            context["error_register"] = "A senha deve conter pelo menos um número."
            return render(request, "introduction/home.html", context)

        if not re.search(r"[@$!%*?&]", password1):
            context["error_register"] = "A senha deve conter pelo menos um caractere especial (@, $, !, %, *, ?, &)."
            return render(request, "introduction/home.html", context)

        if User.objects.filter(username=username).exists():
            context["error_register"] = "Nome de usuário já existe."
            return render(request, "introduction/home.html", context)

        # 4️⃣ E-mail já existe
        if User.objects.filter(email=email).exists():
            context["error_register"] = "E-mail já cadastrado em outra conta."
            return render(request, "introduction/home.html", context)
        # 6️⃣ Autenticar e redirecionar
        login(request, user)
        return redirect("home")

    return render(request, "introduction/home.html")

def erro_login(request):
    return render(request, 'introduction/error/login_error.html')