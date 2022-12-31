from django.shortcuts import render,redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from django.views.generic import TemplateView

# Create your views here.

def home(request):
	context = {}
	return render(request,'pages/home.html',context)

class HomePageView(TemplateView):
	template_name = "pages/home.html"


class AboutPageView(TemplateView):
	template_name = "pages/about.html"


def about(request):
	context = {'page_title':'About'}
	return render(request,'pages/about.html',context)

def contact(request):
	context = {'page_title':'Contact'}
	if request.method == "POST":
		form_data = ContactForm(request.POST)
		if form_data.is_valid():
			new_form = form_data.save()
			messages.success(request,"Message was sent successfully")
	context['form'] = ContactForm()
	return render(request,'pages/contact.html',context)

def terms(request):
	context = {'page_title':'Terms'}
	return render(request,'pages/terms.html',context)


def faq(request):
	context = {'page_title':'FAQ'}
	return render(request,'pages/faq.html',context)


def privacy(request):
	context = {'page_title':'Privacy Policy '}
	return render(request,'pages/privacy.html',context)