from django import forms
from crispy_forms.layout import Column, Layout, Row, Fieldset
from crispy_forms.helper import FormHelper

students = (
    ("STUDENT", "Aluno 1"),
    ("STUDENT", "Aluno 2"),
    ("STUDENT", "Aluno 3"),
    ("STUDENT", "Aluno 4"),
)

class LendingCreateForm(forms.Form):
    student = forms.ChoiceField(
        label="Aluno",
        choices=students,
        widget=forms.Select()
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput()
    )
    initDate = forms.DateField(
        label="Data de Início",
        widget=forms.DateInput()
    )
    finalDate = forms.DateField(
        label="Data de Fim",
        widget=forms.DateInput()
    )


    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        Row(
            Column("student", css_class="col")
        ),
        Row(
            Column("password", css_class="col"),
        ),
        Row(
            Column("initDate", css_class="col-md-6"),
            Column("finalDate", css_class="col-md-6"),
        )
    )
   
