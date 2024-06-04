from django.urls import path
from  recetas.views import index
from recetas.views import Ver_comidasList, Ver_comidasAgregar, Ver_comidaDetalle, Ver_comidaModificar, Ver_comidasBorrar, Ver_sugerenciasList, about_me

app_name = "recetas"

urlpatterns =[
    path("", index, name="index"),
    path("comidas/list", Ver_comidasList.as_view(), name= "lista_comidas"),
    path("comidas/sugerencias", Ver_sugerenciasList.as_view(), name= "lista_sugerencias"),
    path("comidas/detail/<int:pk>", Ver_comidaDetalle.as_view(), name= "detalle_comidas"),
    path("comidas/update/<int:pk>", Ver_comidaModificar.as_view(), name= "modificar_comidas"),
    path("comidas/create", Ver_comidasAgregar.as_view(), name= "agregar_comidas"),
    path("comidas/borrar/<int:pk>", Ver_comidasBorrar.as_view(), name= "borrar_comidas"),
    path("nosotros/", about_me, name= "nosotros")
]
