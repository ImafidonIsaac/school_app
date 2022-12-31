from django.urls import path
from .views import (AboutPageView, HomePageView, home, terms, privacy, contact, about) 

app_name = "pages"

urlpatterns = [
	path('', home, name='home'),
	path('terms-and-conditions/', terms, name='terms'),
	path('faq/', terms, name='faq'),
	# path('terms-and-conditions/', terms, name='terms'),
	path('privacy-policy/', privacy, name='privacy'),
	path('contact/', contact, name='contact'),
	path('about/', about, name='about'),

]
