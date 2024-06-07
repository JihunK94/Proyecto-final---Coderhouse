from django.db import models
import datetime

class Comidas_coreanas(models.Model):
    nombre = models.CharField(max_length= 255, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
class Picante(models.Model):
    nombre = models.CharField(max_length= 255)

    def __str__(self) -> str:
        return self.nombre

class Categorias_comida(models.Model):
    nombre = models.CharField(max_length= 255, unique=True)

    def __str__(self) -> str:
        return self.nombre 
    
class Ver_comidas(models.Model):
    comidas = models.CharField(max_length=50)
    picante = models.CharField(max_length=50)
    categorias = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.comidas

class Ver_sugerencias(models.Model):
    pedido = models.CharField(max_length=500)
    fecha = models.DateField(default=datetime.date.today)
    numero = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return f"{self.numero} - {self.pedido}"


