
from django.contrib import admin
from django.urls import path
from aplicacion_5.views import primeraFuncion
from aplicacion_5.views import formularioContacto
from aplicacion_5.views import informeUsuarios
from aplicacion_5.views import user_login, registro
from django.contrib.auth import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primeraFuncion, name = 'index'),
    path('registro_clientes/login/', primeraFuncion, name = 'index'),
    path('salida_clientes/login/', primeraFuncion, name = 'index'),
    path('registro_clientes/', formularioContacto, name = 'registro_clientes'),
    path('salida_clientes/', informeUsuarios, name = 'salida_clientes'),
    path('login/', user_login, name = 'login'),
    path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
]

