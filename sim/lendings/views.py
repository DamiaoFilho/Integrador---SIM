from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import FormView
from ..core.views import ListView, TableListView
from .models import Lending

from .tables import LendingTable
from django_tables2 import SingleTableView
from .tables import LendingFilter
# Create your views here.


    
class LendingListView(TableListView):
    model = Lending
    template_name = "lendings/lendings_list.html"
    table_class = LendingTable
    paginate_by = 10
    filterset_class = LendingFilter

    def get_queryset(self) -> QuerySet[Any]:
        query = Lending.objects.filter(status=Lending.StatusChoices.IN_PROGRESS)

        return query


class LendingRequestsListView(TableListView):
    model = Lending
    template_name = "lendings/solicitations_list.html"
    table_class = LendingTable
    paginate_by = 10
    filterset_class = LendingFilter

    def get_queryset(self) -> QuerySet[Any]:
        query = Lending.objects.filter(status=Lending.StatusChoices.IN_ANALISYS)

        return query

class LendingStudentListView(TableListView):
    model = Lending
    template_name = "lendings/solicitations_list.html"
    table_class = LendingTable
    paginate_by = 10
    filterset_class = LendingFilter

    def get_queryset(self) -> QuerySet[Any]:
        query = Lending.objects.filter(student=self.request.user.StudentUser.first())

        return query
    


