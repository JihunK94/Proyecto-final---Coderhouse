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

class Ver_sugerencias(models.Model):
    comida_categoria_picante = models.CharField(max_length=500)
    fecha_publicación = models.DateField()
    sugerencia_numero = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self) -> str:
        return f"{self.sugerencia_numero} - {self.comida_categoria_picante}"


