from django import forms

class ReservaForm(forms.Form):
    num_persones = forms.IntegerField(label='Número de personas', min_value=1)
    data_inici = forms.DateField(label='Fecha de inicio', widget=forms.SelectDateWidget)
    data_fi = forms.DateField(label='Fecha de fin', widget=forms.SelectDateWidget)

