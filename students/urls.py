from django.urls import path

from .views import StudentListView, StudentDetailView
app_name = "students"

urlpatterns = [
	path("", StudentListView.as_view(), name="student_list"),
	path("<uuid:pk>/", StudentDetailView.as_view(), name="student_detail"),

]