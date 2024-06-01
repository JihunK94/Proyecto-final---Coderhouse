from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar_usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name= "Avatar", null=True)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    def __str__(self) -> str:
        if self.usuario:
            return self.usuario.username
        return "Sin usuario"

    class Meta:
        verbose_name = "Avatar de usuario"
        verbose_name_plural = "Avatares de usuarios"