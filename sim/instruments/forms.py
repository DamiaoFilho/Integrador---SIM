from django import forms
from crispy_forms.layout import Column, Layout, Row, Fieldset
from crispy_forms.helper import FormHelper

class InstrumentForm(forms.Form):
    image = forms.ImageField(
        label="Imagem",
        widget=forms.FileInput()
    )
    name = forms.CharField(
        label="Nome",
        widget=forms.TextInput()
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
        widget=forms.Textarea()
    )
    documents1 = forms.FileField(
        label="Anexo 1",
        required=False,
    )
    documents2 = forms.FileField(
        label="Anexo 2",
        required=False,
    )
    
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Fieldset(
            Row(
                Column("image", css_class="col")
            ),
            Row(
                Column("image", css_class="col"),
            ),
            Row(
                Column("name", css_class="col"),
            ),
            Row(
                Column("model", css_class="col-md-4"),
                Column("serial_number", css_class="col-md-4"),
                Column("color", css_class="col-md-4"),
            ),
            Row(
                Column("category", css_class="col")
            ),
            Row(
                Column("status", css_class="col")
            ),
            Row(
                Column("documents1", css_class="col-md-6"),
                Column("documents2", css_class="col-md-6"),
            ),
        ),
    )
   
