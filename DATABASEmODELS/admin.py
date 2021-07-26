from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_header = 'JOHN MUIA'

admin.site.register(SINGER)
admin.site.register(SONG)
