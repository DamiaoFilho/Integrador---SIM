
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path("add/", InstrumentCreateView.as_view(), name="add"),
    path("list/", InstrumentListView.as_view(), name="list"),
    path("update/<int:pk>", InstrumentUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", InstrumentDeleteView.as_view(), name="delete")
] 