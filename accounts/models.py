from django.db import models
from django.contrib.auth.models import User



class Destinacio(models.Model):
    nom = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} ({self.pais.upper()})"


class Viatge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="viatges")
    destinacio = models.ForeignKey(Destinacio, on_delete=models.CASCADE, related_name="viatges")
    data_inici = models.DateField()
    data_fi = models.DateField()
    num_persones = models.PositiveIntegerField()
    descripcio = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.destinacio} ({self.data_inici} - {self.data_fi})"

class PerfilUsuari(models.Model):
    usuari = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    nom_complet = models.CharField(max_length=200, blank=True, null=True)  #
    pais_origen = models.CharField(max_length=100, blank=True, null=True)
    data_naixement = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuari.username}"

# Create your models here.
