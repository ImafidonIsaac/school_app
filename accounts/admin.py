from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin



class UserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email','account_type','date_joined']
    list_editable = ['account_type',]

    #We are overiding the variable with our own
    #FORM TO ADD NEW USER FROM THE ADMIN
    add_fieldsets = (

        ('LOGIN DETAILS ', {
            'classes': ('wide',),
            'fields': ('username','email','password1', 'password2',)}
        ),

        ('PERSONAL DETAILS ', {
            'classes': ('wide',),
            'fields': ('first_name','last_name','nick_name','gender','phone_number')}
        ),

    )

    #We are adding our fields to the existing one
    #FORM TO EDIT USER FROM THE ADMIN
    fieldsets = UserAdmin.fieldsets + (

            ('PROFILE DETAILS', {'fields': ('profile_picture','nick_name',
            	'gender','occupation','nationality')}),

            ('PERSONAL DETAILS', {'fields': ('phone_number','residential_address',
            	'place_of_work','state_of_origin','religion')}),

            ('ACCOUNT TYPE', {'fields': ('account_type',)}),
    )
    search_fields = ('email','username','nick_name',)
admin.site.register(User, UserAdmin)