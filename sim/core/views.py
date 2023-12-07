from django.shortcuts import render
from django.views.generic import CreateView as DjangoCreateView
from django.views.generic import ListView as DjangoListView
from django.views.generic import DeleteView as DjangoDeleteView
from django.views.generic import UpdateView as DjangoUpdateView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from ..instruments.models import Instrument

class UpdateView(LoginRequiredMixin, DjangoUpdateView):
    login_url = "/login/"

class CreateView(LoginRequiredMixin, DjangoCreateView):
    login_url = "/login/"

class DeleteView(LoginRequiredMixin, DjangoDeleteView):
    login_url = "/login/"

class ListView(LoginRequiredMixin, DjangoListView):
    login_url = "/login/"

class DashBoardView(ListView):
    model = Instrument
    template_name = "core/dashboard.html"


class TableListView(SingleTableMixin, FilterView):
    pass