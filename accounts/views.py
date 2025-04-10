from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import ReservaForm
from .models import *
from . import forms

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

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Viatge, Destinacio
from .forms import ReservaForm

@login_required
def reserva(request, viatge_nom):
    destinacio = get_object_or_404(Destinacio, nom=viatge_nom)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            num_persones = form.cleaned_data['num_persones']
            data_inici = form.cleaned_data['data_inici']
            data_fi = form.cleaned_data['data_fi']

            reserva = Viatge(
                user=request.user,
                destinacio=destinacio,
                num_persones=num_persones,
                data_inici=data_inici,
                data_fi=data_fi,
                descripcio=f"Reserva realitzada per {num_persones} persones."
            )
            reserva.save()

            # Mostrar página de éxito con los detalles de la reserva
            return render(request, 'reserva_exitosa.html', {'viatge': reserva, 'reserva': reserva})

    else:
        form = ReservaForm()

    # Enviar el formulario en caso de que sea un GET o el formulario no sea válido
    return render(request, 'reserva_form.html', {'form': form, 'viatge': destinacio})

