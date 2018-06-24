from django.urls import path
from Rent import views


urlpatterns = [
    path('index', views.index, name="cars"),
    path('agregar_auto', views.car_add, name="car_add"),
    path('lista_autos', views.list_cars, name="list_cars"),
    path('editar_auto/<int:car_id>', views.edit_car, name="edit_car"),
    path('delete_car/<int:id>', views.delete_car, name="delete_car"),
    path('agregar_ejecutivo', views.executive_add, name="executive_add"),
    path('lista_ejecutivos', views.list_executives, name="list_executives"),
    path('editar_ejecutivo/<int:exe_id>', views.edit_executive, name="edit_executive"),
    path('delete_ejecutive/<int:id>', views.delete_executive, name="delete_executive"),
    path('agregar_cliente', views.client_add, name="client_add"),
    path('lista_clientes', views.list_clients, name="list_clients"),
    path('editar_cliente/<int:cli_id>', views.edit_client, name="edit_client"),
    path('delete_cliente/<int:id>', views.delete_client, name="delete_client"),
]