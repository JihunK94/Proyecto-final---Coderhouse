from django.contrib import admin
from .models import Avatar_usuario
# Register your models here.

admin.site.register(Avatar_usuario)

class Avatar_usuarioAdmin(admin.ModelAdmin):
    list_display = (
        "username"
        "email"
        "profile_image"
    )