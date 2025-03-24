from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
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
def eliminar_viatge(request, viatge_id):
    viatge = get_object_or_404(Viatge, id=viatge_id)
    viatge.delete()
    return redirect('/accounts/profile')
