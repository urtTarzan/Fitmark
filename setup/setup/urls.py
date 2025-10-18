"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from introduction import views
from principal.views import home,logout_view
from django.shortcuts import redirect

urlpatterns = [
    # redireciona a URL base para introduction
    path('', lambda request: redirect('introduction_home')),

    # publicas
    path('admin/', admin.site.urls),
    path('introduction/', views.home_introduction, name='introduction_home'),
    path('parceria/', views.parceria, name='parceria'),
    path('sobre/', views.sobre, name='sobre'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  

    # erro
    path('erro-login/', views.erro_login, name='erro_login'),

    # login necessario
    path('home/', home, name='home'),  
    path("logout/", logout_view, name="logout"),
]


from django.conf.urls import handler404

def redirecionar_404(request, exception):
    return redirect('introduction_home')

handler404 = 'setup.urls.redirecionar_404'