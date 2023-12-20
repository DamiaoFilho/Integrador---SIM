from django.urls import path

from sim.users.views import (
    user_detail_view,
    user_redirect_view,
    StudentUpdateView,
    ProfessorUpdateView,
    StudentListView,
    ChangeStudentGroupView
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("student/update/", StudentUpdateView.as_view(), name="studentUpdate"),
    path("professor/update/", ProfessorUpdateView.as_view(), name="professorUpdate"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("student/list", StudentListView.as_view(), name="studentList"),
    path("student/changeGroup/<int:pk>", ChangeStudentGroupView.as_view(), name="studentChangeGroup")
]
