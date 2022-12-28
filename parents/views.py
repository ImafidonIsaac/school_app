from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from decimal import Decimal
from django.conf import settings
from allauth.account.forms import ChangePasswordForm


from custom_decorators.decorators import parent
# from .forms import ParentProfileForm
# from .models import Parent
# from admission_form.forms import EntranceForm
# from students.models import Student,StudentBioData


@login_required
@parent
def parent_dashboard(request):
	context = {'page_title':"parent Dashboard"}
	context['user'] = request.user
	return render(request,"parents/parent_dashboard.html",context)


# @login_required
# @parent
# def your_kids(request):
# 	context = {'page_title':"Your Kids "}
# 	parent_profile =Parent.objects.get(user=request.user)
# 	students_profile = Student.objects.filter(parent=parent_profile)
# 	context['students_profile'] = students_profile
# 	return render(request,"parent/your_kids.html",context)




# @login_required
# @parent
# def collect_form(request):
# 	context = {'page_title':'Admission Form'}
# 	context['entrance_form'] = EntranceForm()
# 	if request.method == 'POST':
# 		form = EntranceForm(request.POST)
# 		if form.is_valid():
# 			# number_enter = Decimal(form.cleaned_data.get('number_of_form'))
# 			form_data = form.save(commit=False)
# 			form_data.collect_by = request.user
# 			form_data.save()
# 			return redirect('payment:make_payment', form_data.identifier,
# 			 form_data.source_reference)
# 		else:
# 			messages.error(request,"Something Not Right")
# 	return render(request,'parent/collect_form.html',context)


# @login_required
# @parent
# def parent_particular_form(request):
# 	context = {'page_title':"parent Form"}
# 	user=request.user
# 	#If parent details already exist jump to pupils particular
# 	if user.parent_form:
# 		return redirect("student:pupil_particulars_form")
# 	else:
# 		if request.method == "POST":
# 			form = ParentForm(request.POST)
# 			if form.is_valid():
# 				form_data = form.save(commit=False)
# 				form_data.user = user
# 				form_data.save()
# 				return redirect("student:pupil_particulars_form")
# 		else:
# 			context['form'] = ParentForm()
# 	return render(request,"parent/parent_particular_form.html",context)



