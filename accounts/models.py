from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from custom_validators.validators import phone_regex

class User(AbstractUser):
	GENDER = [("Male", "Male"), ("Female", "Female")]
	account_choices = (
		('Admin', 'Admin'),('Principal','Principal'),('Staff','Staff'),
		('Parent','Parent'),('Student','Student'),)
	##################################################################
	nick_name = models.CharField(max_length=200, blank=True,
		help_text="What people know you as ")
	profile_picture = ThumbnailerImageField(upload_to='users/profile_picture',
		null=True,blank=True)
	account_type = models.CharField(choices=account_choices,max_length=40,default="Parent")
	phone_number = models.CharField(validators=[phone_regex],max_length=15,blank=True)
	residential_address = models.CharField(max_length=300,blank=True)
	gender = models.CharField(max_length=10, choices=GENDER, blank=True)
	occupation = models.CharField(max_length=250,blank=True)
	place_of_work = models.CharField(max_length=250,blank=True)
	state_of_origin = models.CharField(max_length=250,blank=True)
	nationality = models.CharField(max_length=250,blank=True)
	religion = models.CharField(max_length=250,blank=True)

	def __str__(self):
		return f"[{self.account_type} Account] {self.username}"