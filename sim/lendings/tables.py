import django_tables2 as tables
from .models import Lending
from django_tables2.utils import A
from django_filters import FilterSet


class LendingTable(tables.Table):
    class Meta:
        model = Lending
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ["student", "initDate", "finalDate", "instrument", "status"]



class LendingRequestTable(tables.Table):
    class Meta:
        model = Lending
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ["student", "initDate", "finalDate", "instrument"]



class LendingFilter(FilterSet):
    class Meta:
        model = Lending
        fields = {"student": ["exact"], "initDate": ["exact"]}
