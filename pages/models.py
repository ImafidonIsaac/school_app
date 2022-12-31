from django.db import models

# Create your models here.


class Contact(models.Model):
	full_name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=300)
	message = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.full_name
