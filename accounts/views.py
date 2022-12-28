from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from decimal import Decimal
from django.conf import settings
import requests
from .models import User
from .forms import UserEditForm
from allauth.account.forms import ChangePasswordForm



import datetime
from django.utils import timezone
from datetime import datetime, timedelta



@login_required
def dashboard(request):
	user = get_object_or_404(User,id=request.user.id)
	if user.account_type == "Student":
		return redirect("students:student_dashboard")
	elif user.account_type == "Parent":
		return redirect("parents:parent_dashboard")
	elif user.account_type == "Staff":
		return redirect("staffs:staff_dashboard")
	elif user.account_type == "Principal":
		return redirect("principal:principal_dashboard")
	else:
		return redirect("admin:admin_dashboard")




@login_required
def edit_profile(request):
	context = {'page_title':'Edit Profile'}
	user = request.user
	if request.method == 'POST':
		form = UserEditForm(instance=user, data=request.POST,files=request.FILES)
		if form.is_valid():
			updated_form = form.save(commit=False)
			updated_form.save()
			messages.success(request, 'Profile Updated Successfully')
	else:
		form = UserEditForm(instance=user)
	context['form'] = form
	return render(request,'accounts/edit_profile.html',context)




