# Generated by Django 4.1.4 on 2022-12-28 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_classes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('student_first_name', models.CharField(max_length=100)),
                ('student_last_name', models.CharField(max_length=100)),
                ('student_middle_name', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('passport', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='students/passport')),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('date_of_admission', models.DateField(default=django.utils.timezone.now)),
                ('admission_number', models.CharField(max_length=50, unique=True)),
                ('current_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Suspended', 'Suspended'), ('Expelled', 'Expelled')], default='Active', max_length=10)),
                ('any_illness', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=40)),
                ('explain_if_illness', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='student_classes.studentclass')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_parent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student ',
                'verbose_name_plural': 'Students',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='StudentBulkUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('csv_file', models.FileField(upload_to='students/bulkupload/')),
            ],
        ),
        migrations.CreateModel(
            name='StudentBioData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_birth', models.CharField(blank=True, max_length=300)),
                ('home_town', models.CharField(blank=True, max_length=300)),
                ('LGA_of_Origin', models.CharField(blank=True, max_length=300)),
                ('state_of_Origin', models.CharField(blank=True, max_length=300)),
                ('nationality', models.CharField(blank=True, max_length=300)),
                ('religion', models.CharField(blank=True, max_length=300)),
                ('permanent_home_address', models.CharField(blank=True, max_length=300)),
                ('contact_address', models.CharField(blank=True, max_length=300)),
                ('student_class_entry_in_school', models.CharField(blank=True, max_length=300)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('parental_status', models.CharField(blank=True, choices=[('COMPLETE OPHAN', 'COMPLETE OPHAN'), ('SINGLE PARENT', 'SINGLE PARENT'), ('BOTH ALIVE', 'BOTH ALIVE')], max_length=50)),
                ('submitted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_bio', to='students.student')),
            ],
            options={
                'verbose_name': 'Student bio data',
                'verbose_name_plural': 'Students bio data',
                'ordering': ['-created'],
            },
        ),
    ]
