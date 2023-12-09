from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from ..core.views import ListView, TableListView, CreateView
from .models import Lending

from .tables import LendingTable
from django_tables2 import SingleTableView
from .tables import LendingFilter
from ..instruments.models import Instrument
from .forms import LendingForm
# Create your views here.

from django_filters.views import FilterView

    
class LendingListView(FilterView, ListView):
    model = Lending
    template_name = "lendings/lendings_in_progress.html"
    paginate_by = 10
    filterset_class = LendingFilter
    
    def get_queryset(self):
        queryset = Lending.objects.filter(status=Lending.StatusChoices.IN_PROGRESS)

        return queryset



class LendingRequestsListView(FilterView, ListView):
    model = Lending
    template_name = "lendings/table_list.html"
    paginate_by = 10
    filterset_class = LendingFilter

    def get_queryset(self) -> QuerySet[Any]:
        query = Lending.objects.filter(status=Lending.StatusChoices.IN_ANALISYS)

        return query

class LendingStudentListView(FilterView, ListView):
    model = Lending
    template_name = "lendings/student_requests.html"
    paginate_by = 10
    filterset_class = LendingFilter

    def get_queryset(self) -> QuerySet[Any]:
        query = Lending.objects.filter(student=self.request.user.StudentUser)

        return query
    


class LendingCreateView(CreateView):
    model = Lending
    template_name = "lendings/form.html"
    success_url = "/instruments/list/"
    form_class = LendingForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        lending = form.save(commit=False)
        lending.student = self.request.user.StudentUser
        instrument = Instrument.objects.get(pk=self.kwargs['pk'])
        instrument.status = False
        instrument.save()
        lending.instrument = instrument

        lending.save()
        return redirect(self.success_url)

