from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
# Create your views here.
@login_required
def home(request):
    return render(request, 'principal/home.html')

def logout_view(request):
    logout(request)
    return redirect('introduction_home')