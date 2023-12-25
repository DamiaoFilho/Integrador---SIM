from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InstrumentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Instrument
# Create your views here.
from django_filters.views import FilterView

from .tables import InstrumentFilter
from ..core.views import CreateView
from ..core.views import DeleteView
from ..core.views import UpdateView
from ..core.views import ListView

class InstrumentCreateView(CreateView):
    model = Instrument
    template_name = "instruments/instrument_create_form.html"
    form_class = InstrumentForm
    success_url = "/instruments/list/"


    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        messages.success(self.request, "Instrumento criado com sucesso")
        return response



class InstrumentListView(FilterView, ListView):
    model = Instrument
    template_name = "instruments/instruments_list.html"
    paginate_by = 3
    filterset_class = InstrumentFilter

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)

class InstrumentUpdateView(UpdateView):
    model = Instrument
    fields = ["image", "name", "model", "brand", "serial_number", "color", "condition"]
    template_name = "instruments/instrument_create_form.html"
    success_url = "/instruments/list"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, f"Instrumento atualizado com sucesso")
        return super().form_valid(form)

class InstrumentDeleteView(DeleteView):
    model = Instrument
    success_url = "/instruments/list/"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.delete(self.request, self.get_object())
        messages.success(self.request, "Instrumento deletado com sucesso")
        return redirect(self.success_url)


