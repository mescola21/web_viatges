from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import *

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sessió automàticament
            return redirect('/')  # Redirigeix a la pàgina principal
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



@login_required
def viatges_programats(request):
    viatges = Viatge.objects.filter(user=request.user)
    return render(request, 'viatges_programats.html', {'viatges': viatges })

@login_required
def perfil(request):
    viatges = Viatge.objects.filter(user=request.user)
    return render(request, 'perfil.html', {'user' : request.user, 'viatges' : viatges })

@login_required
def llista_viatges(request):
    viatges = Destinacio.objects.all()
    return render(request, 'opcions_viatge.html', {'viatges': viatges})

@login_required
def cerca_viatges(request, name):
    name = name.lower()
    viatges = Destinacio.objects.filter(name=name)
    return render(request, 'opcions_viatge.html', {'viatges': viatges})