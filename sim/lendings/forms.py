from django import forms
from crispy_forms.layout import Column, Layout, Row, Fieldset
from crispy_forms.helper import FormHelper
from .models import Lending, Return


class LendingForm(forms.ModelForm):
    class Meta:
        model = Lending
        fields = ["initDate", "finalDate", "justify"]


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        exclude = ["lending"]