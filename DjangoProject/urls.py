from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Importa HttpResponse per a la vista principal
from django.shortcuts import render
from django.urls import path


# Vista per a la pàgina principal
def home(request):
    return render(request, 'home.html')



urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta per al panell d'administració
    path('accounts/', include('accounts.urls')),  # Inclou les rutes de l'app accounts
    path('', home, name='home'),  # Ruta per al camí buit (pàgina principal)
    # ... altres rutes
]
