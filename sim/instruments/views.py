from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import InstrumentForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class InstrumentAddView(LoginRequiredMixin, FormView):
    template_name = "instrument_create_form.html"
    form_class = InstrumentForm
    success_url = "/"
