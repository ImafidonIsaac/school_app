import uuid
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


from website import settings
from easy_thumbnails.fields import ThumbnailerImageField
from parents.models import Parent

from student_classes.models import StudentClass
# from class_room.models import ClassRoom


# Create your models here.
class Student(models.Model):
	ILLNESS_CHOICES = (('Yes', 'Yes'),('No', 'No'),)
	STATUS_CHOICES = [("Active", "Active"),("Inactive", "Inactive"),
	("Suspended", "Suspended"),("Expelled", "Expelled"),]
	GENDER_CHOICES = [("Male", "Male"), ("Female", "Female")]
	##########################################################
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	student_first_name = models.CharField(max_length=100)
	student_last_name = models.CharField(max_length=100)
	student_middle_name = models.CharField(max_length=100, blank=True)
	parent = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,related_name="student_parent")
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES,blank=True)
	passport = ThumbnailerImageField(upload_to='students/passport',
		null=True,blank=True)
	date_of_birth = models.DateField(default=timezone.now)
	#############################################################
	current_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE,
		related_name="student_class")
	# class_room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL,
 #     	blank=True, null=True,related_name="student_class_room")
	date_of_admission = models.DateField(default=timezone.now)
	admission_number = models.CharField(max_length=50, unique=True)
	##########################################################################
	current_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Active")
	any_illness = models.CharField(choices=ILLNESS_CHOICES,max_length=40,default="No")
	explain_if_illness = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created",]
		# ordering = ["surname", "firstname", "other_name"]
		verbose_name = 'Student '
		verbose_name_plural = 'Students'

	def __str__(self):
		return f"{self.student_first_name} {self.student_last_name}"

	def get_absolute_url(self):
		return reverse("students:student_detail", args=[str(self.id)])


    #I use this to change the color in the all kids page
	def badge_color(self):
		if self.current_status == "Active":
			return "low"
		elif self.current_status == "Suspended":
			return "medium"
		else:
			return "high"



'''
#PupilsParticulars is same with StudentProfile
# A student can have only one profile

Those fields that appears also in bio data are not editable by the parents 
only by the Admin
'''




'''
Not Editable only by the admin
Admission form when submitted is seen by the admin
A parent can have multiple bio link to him
But a student can have only one bio

I did not repeat the informations already on the Student Model since its OneToOne
but i also do it that those fields can't be edited by the student/parents

Also those informations relating to parents are already been move to the Parent Model
to advoid repetition
'''
class StudentBioData(models.Model):
	parental_choices = (
		('COMPLETE OPHAN', 'COMPLETE OPHAN'),
		('SINGLE PARENT', 'SINGLE PARENT'),
		('BOTH ALIVE', 'BOTH ALIVE'),)

	student = models.OneToOneField(Student,on_delete=models.SET_NULL,
		related_name="student_bio",null=True,blank=True)
	#########################################################
	place_of_birth = models.CharField(max_length=300,blank=True)
	home_town = models.CharField(max_length=300,blank=True)
	LGA_of_Origin = models.CharField(max_length=300,blank=True)
	state_of_Origin = models.CharField(max_length=300,blank=True)
	nationality = models.CharField(max_length=300,blank=True)
	religion = models.CharField(max_length=300,blank=True)
	permanent_home_address = models.CharField(max_length=300,blank=True)
	contact_address = models.CharField(max_length=300,blank=True)
	student_class_entry_in_school = models.CharField(max_length=300,blank=True)
	email_address = models.EmailField(null=True,blank=True)
	parental_status = models.CharField(choices=parental_choices,max_length=50,
		blank=True)
	##########
	#If submitted it won't be editable to the parent again, unless admin mark as False
	submitted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created']
		verbose_name = 'Student bio data'
		verbose_name_plural = 'Students bio data'

	def __str__(self):
		return f"{self.student.user.first_name} {self.student.user.last_name} Bio Data"



class StudentBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="students/bulkupload/")

