from .models import User
from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _ 
from django.shortcuts import render,redirect, get_object_or_404
from allauth.account.forms import SignupForm




# My own custom  widget for datetime
class DateInput(forms.DateInput):
    input_type = 'date'


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','nick_name')
        # widgets = {'date_of_birth':DateInput()}
