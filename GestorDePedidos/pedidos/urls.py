from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:id_pedido>", views.pedido, name="pedido"),
    path('crear_pedido/', views.crear_pedido, name="crear_pedido"),
    path("modificar_pedido/<int:pedido_id>", views.modificar_pedido, name="modificar_pedido"),
    path('crear_cliente/', views.crear_cliente, name="crear_cliente"),
    path('eliminar_pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido')
]