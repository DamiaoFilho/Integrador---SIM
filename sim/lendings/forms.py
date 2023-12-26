from django import forms
from crispy_forms.layout import Column, Layout, Row, Fieldset
from crispy_forms.helper import FormHelper
from .models import Lending, Return


class LendingForm(forms.ModelForm):
    class Meta:
        model = Lending
        fields = ["initDate", "finalDate", "justify"]
    
        widgets = {
            "initDate": forms.DateInput(attrs={"type": "date"}),
            "finalDate": forms.DateInput(attrs={'type': 'date'}),
        }


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        exclude = ["lending"]        

        widgets = {
            "date": forms.DateInput(attrs={"type":"date"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        Row(
            Column("date", css_class="col-sm-12 col-md-6"),
            Column("photo", css_class="col-sm-12 col-md-6"),
        ),
        Row(
            Column("commentary", css_class="col-sm-12 col-md-12"),
        ),
        )
