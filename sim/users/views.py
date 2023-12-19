from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import models
from django.forms.forms import BaseForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, FormView, CreateView
User = get_user_model()
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.views.generic import UpdateView
from .forms import StudentUserForm
from ..users.models import Student, Professor
from .forms import StudentForm, UserForm, StudentUpdateForm, ProfessorUpdateMultiForm, StudentMultiUpdateForm

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentMultiUpdateForm
    success_message = ("Informações Atualizadas com sucesso")
    template_name = "users/profile.html"
    success_url = "/users/student/update/"
    
    def get_form_kwargs(self):
        kwargs = super(StudentUpdateView, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object.user,
            'student': self.object,
        })
        return kwargs
    
    def get_object(self):
        return self.request.user.StudentUser


class ProfessorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Professor
    form_class = ProfessorUpdateMultiForm
    success_message = ("Informações Atualizadas com sucesso")
    template_name = "users/profile.html"
    success_url = "/users/professor/update/"
    
    def get_form_kwargs(self):
        kwargs = super(StudentUpdateView, self).get_form_kwargs()
        kwargs.update(instance={
            'user': self.object.user,
            'professor': self.object,
        })
        return kwargs
    
    def get_object(self):
        return self.request.user.ProfessorUser



class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


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
        return redirect(self.success_url)
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)

