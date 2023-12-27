from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView as DjangoCreateView
from django.views.generic import ListView as DjangoListView
from django.views.generic import DeleteView as DjangoDeleteView
from django.views.generic import UpdateView as DjangoUpdateView
from django.views.generic import DetailView as DjangoDetailView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from ..lendings.models import Lending
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

class DetailView(LoginRequiredMixin, DjangoDetailView):
    login_url = "/login/"

class DashBoardView(ListView):
    model = Instrument
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        instruments = Instrument.objects.all()
        instrumentsReady = Instrument.objects.filter(status=True)
        lendings = Lending.objects.filter(active=True)

        if hasattr(self.request.user, "StudentUser"):
            studentLendings = len(Lending.objects.filter(student=self.request.user.StudentUser))
        else:
            studentLendings = None

        penalty_end = None
        if hasattr(self.request.user, "StudentUser"):
            student = self.request.user.StudentUser
            if student.has_penalty:
                penalty_end = student.penalty_end


        context["penalty_end"] = penalty_end
        context["instruments"] = len(instruments)
        context["instrumentsReady"] = len(instrumentsReady)
        context["lendings"] = len(lendings)
        context["studentLendings"] = studentLendings

        return context


class TableListView(SingleTableMixin, FilterView):
    pass

