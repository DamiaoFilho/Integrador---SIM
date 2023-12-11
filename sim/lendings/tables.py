import django_tables2 as tables
from .models import Lending, Return
from django_tables2.utils import A
import django_filters

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



class LendingFilter(django_filters.FilterSet):
    student__user__username = django_filters.CharFilter(lookup_expr='icontains', label='Aluno')

    class Meta:
        model = Lending
        fields = ["student__user__username", "student", "initDate"]

class LendingFilter(django_filters.FilterSet):
    student__user__username = django_filters.CharFilter(lookup_expr='icontains', label='Aluno')

    class Meta:
        model = Lending
        fields = ["student__user__username", "student", "initDate"]


class ReturnFilter(django_filters.FilterSet):
    class Meta:
        model = Return
        fields = ["date", "lending"]