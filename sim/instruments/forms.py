from django import forms
from crispy_forms.layout import (
    HTML,
    ButtonHolder,
    Column,
    Div,
    Fieldset,
    Layout,
    Row,
    Submit,
)


class InstrumentForm(forms.Form):
    image = forms.FileField(
        label="Imagem",
        widget=forms.FileInput(
            attrs={"class": "col"}
        )
    )
    name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(
            attrs={"class":"col"}
        )
    )
    model = forms.CharField(
        label="Modelo",
    )
    serial_number = forms.IntegerField(
        label="Número de Série",
    )
    color = forms.CharField(
        label="Cor",
    )
    category = forms.CharField(
        label="Categoria",
    )
    status = forms.CharField(
        label="Estatus",
    )
    documents1 = forms.FileField()
    documents2 = forms.FileField()
    
   
