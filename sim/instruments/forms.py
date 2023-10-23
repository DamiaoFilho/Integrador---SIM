from django import forms

class InstrumentForm(forms.Form):
    image = forms.ImageField(
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
        label="Status",
    )
    documents1 = forms.FileField(
        label="Anexo 1",
        required=False,
    )
    documents2 = forms.FileField(
        label="Anexo 2",
        required=False,
    )
    
   
