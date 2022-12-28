# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator
# from easy_thumbnails.fields import ThumbnailerImageField
# from django.db.models.signals import pre_delete,post_delete,post_save,pre_save,m2m_changed
# from django.dispatch import receiver
# from django.utils.crypto import get_random_string
# from django.shortcuts import get_object_or_404


# #Assignment later move ur signal to signal.py file
# from .models import User
# from students.models import Student,StudentBioData
# from parents.models import Parent
# from staffs.models import Staff
# # from admission_form.models import AdmissionForm
# # from payment.models import Payment



# '''
# On this file you will noticed me using both post_save and pre_save signal the
# ensence is that if you want to do sth b4 object is save you use pre_save but if
# you want to do sth only after its save you use post_save signal
# '''
# @receiver(post_save, sender=User)
# @receiver(post_save, sender=Student)
# # @receiver(post_save, sender=AdmissionForm)
# def do_after_save(sender, instance, created, **kwargs):
# 	'''
# 	Since we are usimg multiple sender, we need to know the sender coming 
# 	b4 we can proceed to do anything
# 	'''
# 	if sender == User:
# 		type_user = instance.group_position
# 		if created:
# 			if type_user == "Parent":
# 				Parent.objects.create(user=instance)
# 			elif type_user == "Student":
# 				Student.objects.create(user=instance)
# 			elif type_user == "Staff":
# 				Staff.objects.create(user=instance)
# 			else:
# 				pass
# 		else:
# 			#If Edited
# 			pass

# 	elif sender == Student:
# 		if created:
# 			StudentBioData.objects.create(student=instance)

# 	else:
# 		pass












# # @receiver(pre_save, sender=User)
# # @receiver(pre_save, sender=AdmissionForm)
# # def do_before_save(sender, instance, **kwargs):
# # 	#If sender is Admission
# # 	if sender == AdmissionForm:
# # 		#If the object is been created
# # 		if instance.id is None:
# # 			Payment.objects.create(payment_source=instance.identifier,
# # 				source_reference=instance.source_reference,
# # 				amount=instance.amount_to_pay,email=instance.collect_by.email)
# # 		#if its object is been edited
# # 		else:
# # 			current_form = instance
# # 			previous_form = AdmissionForm.objects.get(id=instance.id)
# # 			if previous_form.paid != current_form.paid and current_form.paid == True:
# # 				#Create same number of bio data form as the number of form
# # 				#NB: Previous form_number not current one
# # 				parent_profile = ParentProfile.objects.get(
# # 					user=current_form.collect_by)
# # 				for a in range(previous_form.number_of_form):
# # 					StudentBioData.objects.create(parent=parent_profile)

# # 	else:
# # 		pass

# '''
# Once Coin is created we create wallet address for all users
# '''
# # @receiver(post_save, sender=Coin)
# # @receiver(post_save, sender=User)
# # def create_wallet_all_users(sender, instance, created, **kwargs):
# # 	if created:
# # 		'''
# # 		If the object is just created
# # 		'''
# # 		if sender == Coin:
# # 			'''
# # 			If a coin is created create the equivalent wallet for all existing users
# # 			'''
# # 			users = User.objects.all()
# # 			for a in users:
# # 				CoinWallet.objects.create(user=a,coin=instance)

# # 		elif sender == User:
# # 			'''
# # 			Use all existing coin to create wallets for this user
# # 			'''
# # 			coins = Coin.objects.all()
# # 			for a in coins:
# # 				CoinWallet.objects.create(user=instance,coin=a)