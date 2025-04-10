from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

admin.site.register(Viatge)
admin.site.register(Destinacio)
admin.site.register(PerfilUsuari)


# Register your models here.
