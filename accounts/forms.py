from django import forms
from .models import PerfilUsuari

class ReservaForm(forms.Form):
    num_persones = forms.IntegerField(label='Número de personas', min_value=1)
    data_inici = forms.DateField(label='Fecha de inicio', widget=forms.SelectDateWidget)
    data_fi = forms.DateField(label='Fecha de fin', widget=forms.SelectDateWidget)

class PerfilUsuariForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuari
        fields = ['avatar', 'descripcion', 'nom_complet', 'pais_origen', 'data_naixement']
        labels = {
            'avatar': 'Foto de perfil',  # Cambiar el nombre del campo de avatar
            'descripcion': 'Descripció',  # Cambiar el nombre del campo de descripción
            'nom_complet': 'Nom complet',  # Cambiar el nombre del campo de nombre completo
            'pais_origen': 'País d\'origen',  # Cambiar el nombre del campo de país de origen
            'data_naixement': 'Data de naixement',  # Cambiar el nombre del campo de fecha de nacimiento
        }
        help_texts = {
            'avatar': 'Pots pujar una imatge per al teu perfil.',
            'descripcion': 'Afegeix una breu descripció sobre tu.',
            'nom_complet': 'Escriviu el vostre nom complet.',
            'pais_origen': 'Indiqueu el vostre país d\'origen.',
            'data_naixement': 'Introdueix la teva data de naixement.',
        }