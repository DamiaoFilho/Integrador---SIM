from django import forms
from crispy_forms.layout import Column, Layout, Row, Fieldset
from crispy_forms.helper import FormHelper
from .models import Instrument, Category, InstrumentType
from django_select2 import forms as s2forms
from django import forms
class InstrumentForm(forms.ModelForm):

    class Meta:
        model = Instrument
        exclude = ["status"]
