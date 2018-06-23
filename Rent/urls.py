from django.urls import path
from Rent import views


urlpatterns = [
    path('index', views.index, name="cars"),
    path('agregar_auto', views.car_add, name="car_add"),
    path('lista_autos', views.list_cars, name="list_cars"),
    path('editar_auto/<int:car_id>', views.edit_car, name="edit_car"),
    path('delete/<int:id>', views.delete_car, name="delete_car"),
]