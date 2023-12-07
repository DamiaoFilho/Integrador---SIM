from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import *
app_name = "lendings"

urlpatterns = [
    path("requests/", LendingRequestsListView.as_view(), name="requests"),
    path("list/", LendingListView.as_view(), name="list"),
    path("studentRequests/", LendingListView.as_view(), name="studentRequests"),
] 