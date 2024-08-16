
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referencia
    # facebook.com
    path('',views.home, name='home'),
    # usarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]