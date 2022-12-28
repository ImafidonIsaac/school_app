from django.contrib import admin

from .models import StudentClass




@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
	list_display = ['class_long_name','class_short_name','class_name_in_numeric',
		'created','updated']
	search_fields = ['class_long_name','class_short_name','class_name_in_numeric',]