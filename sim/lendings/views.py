from django.shortcuts import render
from django.views.generic import FormView
from .forms import LendingCreateForm

# Create your views here.


class LendingCreateView(FormView):
    form_class = LendingCreateForm
    template_name = "lendings_create_form.html"
    success_url = "lendingslist/"