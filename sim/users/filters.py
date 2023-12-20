import django_filters
from .models import Student


class StudentFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains', label='Nome do Aluno')


    class Meta:
        model = Student
        fields = ["user__username", "year", "shift", "course", "is_colleger"]