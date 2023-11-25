from django import forms
from crispy_forms.layout import Column, Layout, Row, Fieldset
from crispy_forms.helper import FormHelper
from .models import Instrument

class InstrumentForm(forms.ModelForm):

    class Meta:
        model = Instrument
        exclude = ["status"]

    
    layout = Layout(
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
   
