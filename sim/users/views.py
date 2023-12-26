from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import models
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, FormView, CreateView
User = get_user_model()
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.generic import UpdateView
from .forms import StudentUserForm, ProfessorSignUpForm
from ..users.models import Student, Professor
from .forms import StudentForm, UserForm, StudentUpdateForm, ProfessorUpdateMultiForm, StudentMultiUpdateForm
from ..core.views import ListView
from django_filters.views import FilterView
from .filters import StudentFilter, ProfessorFilter
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.mixins import PermissionRequiredMixin
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentMultiUpdateForm
    template_name = "users/profile.html"
    success_url = "/users/student/update/"
    
    def get_form_kwargs(self):
        kwargs = super(StudentUpdateView, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object.user,
            'student': self.object,
        })
        return kwargs
    

    def form_valid(self, form: BaseForm) -> HttpResponse:
        messages.success(self.request, "Perfil atualizado com sucesso")
        return super().form_valid(form)

    def get_object(self):
        return self.request.user.StudentUser


class ProfessorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Professor
    form_class = ProfessorUpdateMultiForm
    success_message = ("Informações Atualizadas com sucesso")
    template_name = "users/profile.html"
    success_url = "/users/professor/update/"
    
    def get_form_kwargs(self):
        kwargs = super(ProfessorUpdateView, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object.user,
            'professor': self.object,
        })
        return kwargs
    
    def form_valid(self, form: BaseForm) -> HttpResponse:
        messages.success(self.request, "Perfil atualizado com sucesso")
        return super().form_valid(form)
    
    def get_object(self):
        return self.request.user.ProfessorUser



class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("home")


user_redirect_view = UserRedirectView.as_view()


class StudentSignUpView(CreateView):
    form_class = StudentUserForm
    template_name = "account/signup.html"
    success_url = "/login/"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        student_group = Group.objects.get(name='student')

        student = form["student"].save(commit=False)
        student.user = form["user"].save(self.request)

        student.user.groups.add(student_group)

        student.save()
        messages.success(self.request, "Novo estudante registrado com sucesso")
        return redirect(self.success_url)
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)



class StudentListView(PermissionRequiredMixin, FilterView, ListView):
    model = Student
    template_name = "users/usersList.html"
    paginate_by = 10
    filterset_class = StudentFilter
    permission_required = "lendings.add_return"

class ChangeStudentGroupView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = "lendings.add_return"

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(pk=self.kwargs['pk'])
        colleger = Group.objects.get(name='colleger')

        groups = student.user.groups.all()

        if colleger in groups:
            messages.success(self.request, "Bolsista removido")
            student.user.groups.remove(colleger)
            student.is_colleger = False
        else:
            messages.success(self.request, "Registrado novo bolsista")
            student.user.groups.add(colleger)
            student.is_colleger = True



        student.save()
        return redirect("/users/student/list")
    


class ProfessorListView(PermissionRequiredMixin, FilterView, ListView):
    permission_required = "lendings.add_return"
    model = Professor
    template_name = "users/professorsList.html"
    paginate_by = 10
    filterset_class = ProfessorFilter

    def get_queryset(self) -> QuerySet[Any]:
        if hasattr(self.request.user, "ProfessorUser"):
            queryset = Professor.objects.exclude(pk=self.request.user.ProfessorUser.pk)
        else:
            queryset = Professor.objects.all()
        return queryset


class ProfessorCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Professor
    template_name = "users/professor_create.html"
    form_class = ProfessorSignUpForm
    permission_required = "lendings.add_return"

    success_url = "/users/professor/list"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        professor_group = Group.objects.get(name='professor')

        professor = form["professor"].save(commit=False)
        professor.user = form["user"].save(self.request)

        professor.user.groups.add(professor_group)

        professor.save()
        messages.success(self.request, "Professor criado com sucesso")
        return redirect(self.success_url)


class LoginView(DjangoLoginView):
    template_name="account/login.html"
    redirect_authenticated_user=True

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        messages.success(self.request, f"Usuário logado com sucesso")
        return super().form_valid(form)
    