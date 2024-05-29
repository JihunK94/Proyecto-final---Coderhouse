from django.db import models

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


