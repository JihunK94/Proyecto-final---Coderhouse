from django.urls import path
from  recetas.views import index, lista_comidas, agregar_comidas, detalle_comidas

app_name = "recetas"

urlpatterns =[
    path("", index, name="index"),
    path("comidas/list", lista_comidas, name= "lista_comidas"),
    path("comidas/create", agregar_comidas, name= "agregar_comidas"),
    path("comidas/detail/<int:pk>", detalle_comidas, name= "detalle_comidas"),
]
