from django import forms
from . import models

class ListacomidasForm(forms.ModelForm):
    class Meta:
        model = models.Ver_comidas
        fields = ["comidas", "categorias", "picante"]
