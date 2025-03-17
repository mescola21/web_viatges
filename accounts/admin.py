from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(Viatge)
admin.site.register(Destinacio)

# Register your models here.
