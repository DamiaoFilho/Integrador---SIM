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
    path("studentRequests/", LendingStudentListView.as_view(), name="studentRequests"),
    path("create/<int:pk>", LendingCreateView.as_view(), name="create"),
    path("returnCreate/<int:pk>", ReturnCreateView.as_view(), name="returnCreate"),
    path("accept/<int:pk>", AcceptView.as_view(), name="accept"),
    path("denied/<int:pk>", DeniedView.as_view(), name="denied"),
    path("cancel/<int:pk>", CancelView.as_view(), name="cancel"),
    path("lending/detail/<int:pk>", LendingDetailView.as_view(), name="detail"),
    path("lending/analysis/<int:pk>", LendingAnalysisView.as_view(), name="analysis"),
    path("returns", ReturnsListView.as_view(), name="returns"),
] 