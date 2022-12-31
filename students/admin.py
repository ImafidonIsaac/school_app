from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display = ['student_first_name','student_last_name','current_class','parent']

admin.site.register(Student, StudentAdmin)