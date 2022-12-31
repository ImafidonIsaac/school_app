from django.shortcuts import render
from .models import Student
from django.views.generic import (TemplateView,ListView, DetailView,CreateView,
	UpdateView, DeleteView, FormView)
from django.views.generic.detail import SingleObjectMixin 
from django.urls import reverse_lazy, reverse
# from .models import Post, Comment
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
# from .forms import CommentForm
from django.views import View
from django.db.models import Q

#TODO: Only show students for this parent
class StudentListView(LoginRequiredMixin, ListView):
	model = Student
	context_object_name = "student_list"
	template_name = "students/student_list.html"
	# queryset = Student.objects.filter(title__icontains="sdsajdhsa")

class SearchStudentListView(LoginRequiredMixin, ListView):
	model = Student
	context_object_name = "student_list"
	template_name = "students/student_list.html"

	def get_queryset(self):
		query = self.request.GET.get("q")
		return Student.objects.filter(
			Q(student_first_name__icontains=query) | Q(student_last_name__icontains=query)
		)



class StudentDetailView(LoginRequiredMixin, DetailView):
	model = Student
	context_object_name = "student"
	template_name = "students/student_detail.html"
	login_url = "account_login"


