from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.lista_clientes , name='mostra_clientes'),
    path('new/', views.add_cliente, name='add_clientes'),
]
