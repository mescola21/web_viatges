from django.db import models
from django.contrib.auth.models import User




class Viatge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="viatges")
    destinacio = models.CharField(max_length=100)
    data_inici = models.DateField()
    data_fi = models.DateField()
    descripcio = models.TextField()

    def __str__(self):
        return f"{self.destinacio} ({self.data_inici} - {self.data_fi})"

# Create your models here.




class Route(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="routes", blank = True, null=True)
    nom = models.CharField(max_length=100)
    descripcio = models.TextField()
    data_creacio = models.DateField()
    destinacions = models.ManyToManyField("Destinacio", related_name="routes")
    defecte = models.BooleanField(default=False)
    origen = models.CharField(max_length=100)
    final= models.CharField(max_length=100)
    imatge = models.ImageField(upload_to="rutes/", blank = True, null = True)

    def __str__(self):
        return f"{self.origen} ({self.final})"


class Destinacio(models.Model):
    nom = models.CharField(max_length=100)
    routeid = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="destinacios", blank=True, null = True)
    pais = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nom} ({self.pais.upper()})"