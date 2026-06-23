
from .models import *

from django.forms import ModelForm
from django import forms

class FormCategorias(ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Categorias
        fields = '__all__'