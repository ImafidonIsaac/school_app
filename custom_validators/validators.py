from django.core.validators import RegexValidator
from easy_thumbnails.fields import ThumbnailerImageField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _


phone_regex = RegexValidator( regex = r'^\+?1?\d{9,14}$',
		message = """Phone number must be entered in the format: 
		'+9999999999'. Up to 14 digits allowed .""")


