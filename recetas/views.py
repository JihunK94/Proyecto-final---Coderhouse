from django.shortcuts import render, redirect
from recetas.models import Ver_comidas
from recetas.forms import ListacomidasForm

def index(request): 
    return render(request, "recetas/index.html")

def lista_comidas(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = Ver_comidas.objects.filter(comidas__icontains=busqueda)
    else:   
        consulta = Ver_comidas.objects.all()  
    contexto = {"comidas":consulta}
    return render(request,"recetas/lista_comidas.html", contexto)

def agregar_comidas(request):
    if request.method == "POST":
        form =  ListacomidasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("recetas:lista_comidas")
    else:
        form = ListacomidasForm()
        return render (request, "recetas/lista_comidas_agregar.html", {"form": form} )
    
def detalle_comidas(request, pk: int):
    consulta = Ver_comidas.objects.get(id=pk)
    contexto = {"detalle" : consulta}
    return render (request, "recetas/lista_comidas_detalles.html", contexto)
    









