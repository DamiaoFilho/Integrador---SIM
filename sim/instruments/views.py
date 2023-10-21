from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import InstrumentForm

# Create your views here.


class InstrumentAddView(FormView):
    template_name = "instrument_create_form.html"
    form_class = InstrumentForm
    success_url = "/"
