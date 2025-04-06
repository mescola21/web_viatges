from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Viatge

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
def opcions_viatge(request):
    if request.method == 'POST':
        destinacio = request.POST['destinacio']
        data_inici = request.POST['data_inici']
        data_fi = request.POST['data_fi']
        descripcio = request.POST.get('descripcio', '')

        Viatge.objects.create(
            user=request.user,
            destinacio=destinacio,
            data_inici=data_inici,
            data_fi=data_fi,
            descripcio=descripcio
        )

        missatge = "Viatge creat correctament!"
        return render(request, 'opcions_viatge.html', {'missatge': missatge})

    return render(request, 'opcions_viatge.html')