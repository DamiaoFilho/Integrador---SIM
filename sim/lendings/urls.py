from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import LendingCreateView
app_name = "lendings"
urlpatterns = [
    path("lendingslist/", TemplateView.as_view(template_name="lendings_list.html"), name="lendingslist"),
    path("add/", LendingCreateView.as_view(), name="lendingAdd")
] 