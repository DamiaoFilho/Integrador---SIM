from django import forms
from crispy_forms.layout import Column, Layout, Row, Fieldset
from crispy_forms.helper import FormHelper
from .models import Lending

students = (
    ("STUDENT", "Aluno 1"),
    ("STUDENT", "Aluno 2"),
    ("STUDENT", "Aluno 3"),
    ("STUDENT", "Aluno 4"),
)

instruments = (
    ("INSTRUMENT", "Violão"),
    ("INSTRUMENT", "Pandeiro"),
    ("INSTRUMENT", "Carillhão"),
    ("INSTRUMENT", "Baixo"),
)


class LendingForm(forms.ModelForm):
    class Meta:
        model = Lending
        fields = ["initDate", "finalDate", "justify"]
   
