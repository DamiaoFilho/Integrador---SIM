from django import forms
from crispy_forms.layout import Column, Layout, Row, Fieldset
from crispy_forms.helper import FormHelper
from .models import Instrument, Category, InstrumentType
from django_select2 import forms as s2forms
from django import forms


class Select2MixIn(s2forms.ModelSelect2MultipleWidget):
    def __init__(self, *args, **kwargs):
        self.search = kwargs.pop("search", False)
        super().__init__(*args, **kwargs)

    def build_attrs(self, base_attrs, extra_attrs=None):
        if extra_attrs is None:
            extra_attrs = {}
        extra_attrs.update({"data-minimum-input-length": 0})
        # if self.search:
        extra_attrs.update({"data-minimum-results-for-search": "Infinity"})
        return super().build_attrs(base_attrs, extra_attrs)

class InstrumentCategoryWidget(Select2MixIn):
    search_fields = [
        "name__icontains",
    ]

class InstrumentTypeWidget(Select2MixIn):
    search_fields = [
        "name__icontains",
    ]


class InstrumentForm(forms.ModelForm):

    class Meta:
        model = Instrument
        exclude = ["status"]

        widgets = {
            "category": InstrumentCategoryWidget(),
            "type": InstrumentTypeWidget()
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
            Column("image", css_class="col-sm-12 col-md-12"),
        ),
        Row(
            Column("name", css_class="col-sm-12 col-md-8"),
            Column("model", css_class="col-sm-12 col-md-4"),
        ),
        Row(
            Column("brand", css_class="col-sm-12 col-md-4"),
            Column("serial_number", css_class="col-sm-12 col-md-4"),
            Column("color", css_class="col-sm-12 col-md-4"),
        ),
        Row(
            Column("category", css_class="col-sm-12 col-md-6"),
            Column("type", css_class="col-sm-12 col-md-6"),
        ),
        Row(
            Column("condition", css_class="col-sm-12 col-md-12"),
        )
        )

