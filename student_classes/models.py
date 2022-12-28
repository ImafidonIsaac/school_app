from django.db import models


'''
Am using this name to avoid error on django keywords restriction
class_name_in_numeric is used to set the ordering
'''
class StudentClass(models.Model) :
    #You can't add same class twice
    class_long_name = models.CharField(max_length=50,unique=True, help_text="E.g Junior Secondary 1")
    class_short_name = models.CharField(max_length=30, help_text="E.g JSS1")
    class_name_in_numeric   =   models.IntegerField(unique=True,help_text='E.g 1,2,4,5 etc')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['class_name_in_numeric',]
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        

    # def get_absolute_url(self):
    #     return reverse('student_classes:class_list')


    def __str__(self):
        return self.class_long_name