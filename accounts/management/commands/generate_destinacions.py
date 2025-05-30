from django.core.management.base import BaseCommand
from accounts.models import *
import random

class Command(BaseCommand):
    help = 'Genera 100 destinos conocidos en la base de datos'

    def handle(self, *args, **kwargs):
        # Lista de destinos conocidos
        destinos_conocidos = [
            ("Madrid", "España", "Europa"),
            ("Barcelona", "España", "Europa"),
            ("Londres", "Reino Unido", "Europa"),
            ("París", "Francia", "Europa"),
            ("Roma", "Italia", "Europa"),
            ("Berlín", "Alemania", "Europa"),
            ("Ámsterdam", "Países Bajos", "Europa"),
            ("Lisboa", "Portugal", "Europa"),
            ("Bruselas", "Bélgica", "Europa"),
            ("Copenhague", "Dinamarca", "Europa"),
            ("Estocolmo", "Suecia", "Europa"),
            ("Viena", "Austria", "Europa"),
            ("Praga", "República Checa", "Europa"),
            ("Budapest", "Hungría", "Europa"),
            ("Dublín", "Irlanda", "Europa"),
            ("Atenas", "Grecia", "Europa"),
            ("Zürich", "Suiza", "Europa"),
            ("Ámsterdam", "Países Bajos", "Europa"),
            ("Múnich", "Alemania", "Europa"),
            ("Bratislava", "Eslovaquia", "Europa"),
            ("Oslo", "Noruega", "Europa"),
            ("Reykjavik", "Islandia", "Europa"),
            ("Dubrovnik", "Croacia", "Europa"),
            ("Dubái", "Emiratos Árabes Unidos", "Asia"),
            ("Estambul", "Turquía", "Asia"),
            ("Beijing", "China", "Asia"),
            ("Tokio", "Japón", "Asia"),
            ("Seúl", "Corea del Sur", "Asia"),
            ("Bangkok", "Tailandia", "Asia"),
            ("Singapur", "Singapur", "Asia"),
            ("Kuala Lumpur", "Malasia", "Asia"),
            ("Hong Kong", "China", "Asia"),
            ("Ho Chi Minh", "Vietnam", "Asia"),
            ("Delhi", "India", "Asia"),
            ("Mumbai", "India", "Asia"),
            ("Lima", "Perú", "América del Sur"),
            ("Buenos Aires", "Argentina", "América del Sur"),
            ("Río de Janeiro", "Brasil", "América del Sur"),
            ("Santiago", "Chile", "América del Sur"),
            ("Montevideo", "Uruguay", "América del Sur"),
            ("Quito", "Ecuador", "América del Sur"),
            ("Caracas", "Venezuela", "América del Sur"),
            ("La Paz", "Bolivia", "América del Sur"),
            ("Ciudad de México", "México", "América del Norte"),
            ("Cancún", "México", "América del Norte"),
            ("Nueva York", "EE. UU.", "América del Norte"),
            ("Los Ángeles", "EE. UU.", "América del Norte"),
            ("Chicago", "EE. UU.", "América del Norte"),
            ("Toronto", "Canadá", "América del Norte"),
            ("Vancouver", "Canadá", "América del Norte"),
            ("San Francisco", "EE. UU.", "América del Norte"),
            ("Miami", "EE. UU.", "América del Norte"),
            ("Washington D.C.", "EE. UU.", "América del Norte"),
            ("Ciudad de Panamá", "Panamá", "América Central"),
            ("San José", "Costa Rica", "América Central"),
            ("La Habana", "Cuba", "Caribe"),
            ("Kingston", "Jamaica", "Caribe"),
            ("San Juan", "Puerto Rico", "Caribe"),
            ("Baja California", "México", "América del Norte"),
            ("Machu Picchu", "Perú", "América del Sur"),
            ("Cuzco", "Perú", "América del Sur"),
            ("Cusco", "Perú", "América del Sur"),
            ("Galápagos", "Ecuador", "América del Sur"),
            ("Montevideo", "Uruguay", "América del Sur"),
            ("Lagos", "Nigeria", "África"),
            ("El Cairo", "Egipto", "África"),
            ("Johannesburgo", "Sudáfrica", "África"),
            ("Nairobi", "Kenia", "África"),
            ("Casablanca", "Marruecos", "África"),
            ("Dakar", "Senegal", "África"),
            ("Zanzíbar", "Tanzania", "África"),
            ("Marrakech", "Marruecos", "África"),
            ("Túnez", "Túnez", "África"),
            ("Luanda", "Angola", "África"),
            ("Santiago de Compostela", "España", "Europa"),
            ("Mallorca", "España", "Europa"),
            ("Islas Canarias", "España", "Europa"),
            ("Lagos", "Nigeria", "África"),
            ("Mombasa", "Kenia", "África"),
            ("Abuja", "Nigeria", "África"),
            ("Cairo", "Egipto", "África"),
            ("Zanzibar", "Tanzania", "África"),
            ("Marrakech", "Marruecos", "África"),
            ("Dakar", "Senegal", "África"),
            ("Dar es Salaam", "Tanzania", "África"),
            ("Victoria Falls", "Zambia/Zimbabwe", "África"),
            ("Pretoria", "Sudáfrica", "África")
        ]

        # Generar los destinos en la base de datos
        for nombre, pais, continente in destinos_conocidos:
            Destinacio.objects.create(
                nom=nombre,
                pais=pais,
                continent=continente
            )

        self.stdout.write(self.style.SUCCESS('¡100 destinos generados correctamente!'))
