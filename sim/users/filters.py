import django_filters
from .models import Student, Professor


class StudentFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains', label='Nome do Aluno')


    class Meta:
        model = Student
        fields = ["user__username", "year", "shift", "course", "is_colleger"]


class ProfessorFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains', label='Nome do Professor')

    class Meta:
        model = Professor
        fields = ["user__username", "register", "employee_register"]