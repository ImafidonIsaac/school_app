from django.urls import path
from .views import parent_dashboard

app_name = "parents"

urlpatterns = [
	path('', parent_dashboard, name='parent_dashboard'),
	# path('your-kids', views.your_kids, name='your_kids'),
	# path('form/', views.parent_particular_form, name='parent_particular_form'),
	# path('collect/', views.collect_form, name='collect_form'),
]
