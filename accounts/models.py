from django.db import models
from django.contrib.auth.models import User



class Viatge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="viatges")
    destinacio = models.CharField(max_length=100)
    data_inici = models.DateField()
    data_fi = models.DateField()
    descripcio = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=50 ,blank=True, null=True)
    continent = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return f"{self.destinacio} ({self.data_inici} - {self.data_fi})"



# Create your models here.
