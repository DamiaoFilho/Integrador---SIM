from django.urls import path

from sim.users.views import (
    user_detail_view,
    user_redirect_view,
    StudentUpdateView
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("update/", StudentUpdateView.as_view(), name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
