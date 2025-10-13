from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'introduction/home.html')

def parceria(request):
    return render(request, 'introduction/parceria.html')

def sobre(request):
    return render(request, 'introduction/sobre.html')