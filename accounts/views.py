from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import *
from .forms import *
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            PerfilUsuari.objects.create(
                usuari=user,
                avatar=None,
                descripcion=None,
                nom_complet=None,
                pais_origen=None,
                data_naixement=None
            )
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
    perfil = get_object_or_404(PerfilUsuari, usuari=request.user)
    viatges = Viatge.objects.filter(user=request.user)

    context = {
        'perfil': perfil,
        'viatges': viatges
    }
    return render(request, 'perfil.html', context)

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

            return render(request, 'reserva_exitosa.html', {'viatge': reserva, 'reserva': reserva})

    else:
        form = ReservaForm()

    return render(request, 'reserva_form.html', {'form': form, 'viatge': destinacio})


@login_required
def editar_perfil(request):
    perfil = get_object_or_404(PerfilUsuari, usuari=request.user)

    if request.method == 'POST':
        form = PerfilUsuariForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PerfilUsuariForm(instance=perfil)

    return render(request, 'editar_perfil.html', {'form': form})