from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from recetas.models import Ver_comidas
from recetas.forms import ListacomidasForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

def index(request):
    return render(request, "recetas/index.html")

# def lista_comidas(request):
#     busqueda = request.GET.get("busqueda", None)
#     if busqueda:
#         print(busqueda)
#         consulta = Ver_comidas.objects.filter(comidas__icontains=busqueda)
#     else:
#         consulta = Ver_comidas.objects.all()
#     contexto = {"comidas":consulta}
#     return render(request,"recetas/lista_comidas.html", contexto)

class Ver_comidasList(ListView):
    model = Ver_comidas
    #context_object_name: "comidas"
    template_name = "recetas/lista_comidas.html"
    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("busqueda"):
            busqueda = self.request.GET.get("busqueda")
            consulta = Ver_comidas.objects.filter(comidas__icontains=busqueda)
        else:
            consulta = Ver_comidas.objects.all()
        return consulta

# def agregar_comidas(request):
#      if request.method == "POST":
#          form =  ListacomidasForm(request.POST)
#          if form.is_valid():
#              form.save()
#              return redirect ("recetas:lista_comidas")
#      else:
#          form = ListacomidasForm()
#          return render (request, "recetas/lista_comidas_form.html", {"form": form} )

class Ver_comidasAgregar(CreateView):
     model = Ver_comidas
     form_class = ListacomidasForm
     template_name = "recetas/lista_comidas_form.html"
     success_url = reverse_lazy("recetas:lista_comidas")


# def detalle_comidas(request, pk: int):
#     consulta = Ver_comidas.objects.get(id=pk)
#     contexto = {"detalle" : consulta}
#     return render (request, "recetas/lista_comidas_detalles.html", contexto)

class Ver_comidaDetalle(DetailView):
    model = Ver_comidas
    template_name = "recetas/lista_comidas_detalles.html"

    def get_context_data(self, **kwargs):
        return {"detalle": self.get_object()}








