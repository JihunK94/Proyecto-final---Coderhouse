from django.urls import path
from  recetas.views import index
from recetas.views import Ver_comidasList, Ver_comidasAgregar, Ver_comidaDetalle

app_name = "recetas"

urlpatterns =[
    path("", index, name="index"),
    path("comidas/list", Ver_comidasList.as_view(), name= "lista_comidas"),
    path("comidas/detail/<int:pk>", Ver_comidaDetalle.as_view(), name= "detalle_comidas"),
    path("comidas/create", Ver_comidasAgregar.as_view(), name= "agregar_comidas"),
]
