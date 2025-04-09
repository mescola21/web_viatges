from django.contrib import admin
from .models import Viatge, Route, Destinacio

admin.site.register(Viatge)



@admin.register(Destinacio)
class DestinacioAdmin(admin.ModelAdmin):
    list_display = ('nom', 'pais', 'continent')
    search_fields = ('nom', 'pais')
    list_filter = ('continent',)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'defecte']
    list_filter = ['defecte']


# Register your models here.
