from django import forms
from .models import *

class ReservaForm(forms.Form):
    num_persones = forms.IntegerField(label='Número de personas', min_value=1)
    data_inici = forms.DateField(label='Fecha de inicio', widget=forms.SelectDateWidget)
    data_fi = forms.DateField(label='Fecha de fin', widget=forms.SelectDateWidget)

class PerfilUsuariForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuari
        fields = ['avatar', 'descripcion', 'nom_complet', 'pais_origen', 'data_naixement']
        labels = {
            'avatar': 'Foto de perfil',
            'descripcion': 'Descripció',
            'nom_complet': 'Nom complet',
            'pais_origen': 'País d\'origen',
            'data_naixement': 'Data de naixement',
        }
        help_texts = {
            'avatar': 'Pots pujar una imatge per al teu perfil.',
            'descripcion': 'Afegeix una breu descripció sobre tu.',
            'nom_complet': 'Escriviu el vostre nom complet.',
            'pais_origen': 'Indiqueu el vostre país d\'origen.',
            'data_naixement': 'Introdueix la teva data de naixement.',
        }


class DestinacioForm(forms.ModelForm):
    class Meta:
        model = Destinacio
        fields = ['nom', 'pais', 'continent']

class ViatgeForm(forms.ModelForm):
    class Meta:
        model = Viatge
        fields = ['user', 'destinacio', 'data_inici', 'data_fi', 'num_persones', 'descripcio']

class FlightSearchForm(forms.Form):
    AIRPORT_CHOICES = [
        ("BCN", "Barcelona (BCN)"),
        ("MAD", "Madrid (MAD)"),
        ("VLC", "Valencia (VLC)"),
        ("SVQ", "Sevilla (SVQ)"),
        ("BIO", "Bilbao (BIO)"),
        ("AGP", "Málaga (AGP)"),
        ("PMI", "Palma de Mallorca (PMI)"),
        ("LHR", "Londres (LHR)"),
        ("CDG", "París (CDG)"),
        ("FCO", "Roma (FCO)"),
        ("AMS", "Ámsterdam (AMS)"),
        ("TXL", "Berlín (TXL)"),
        ("LIS", "Lisboa (LIS)"),
        ("PRG", "Praga (PRG)"),
        ("FRA", "Fráncfort (FRA)"),
        ("ZRH", "Zúrich (ZRH)"),
        ("MUC", "Múnich (MUC)"),
        ("BRU", "Bruselas (BRU)"),
        ("VIE", "Viena (VIE)"),
        ("ATH", "Atenas (ATH)"),
        ("CPT", "Ciudad del Cabo (CPT)"),
        ("STO", "Estocolmo (STO)"),
        ("OSL", "Oslo (OSL)"),
        ("HKG", "Hong Kong (HKG)"),
        ("CPH", "Copenhague (CPH)"),
        ("DUB", "Dublín (DUB)"),
        ("SFO", "San Francisco (SFO)"),
        ("YYZ", "Toronto (YYZ)"),
        ("BUD", "Budapest (BUD)"),
        ("SOF", "Sofía (SOF)"),
        ("CGN", "Colonia (CGN)"),
        ("TFS", "Tenerife Sur (TFS)"),
        ("NCE", "Niza (NCE)"),
        ("GVA", "Ginebra (GVA)"),
        ("SJJ", "Sarajevo (SJJ)"),
        ("ARN", "Estocolmo (ARN)"),
        ("TLV", "Tel Aviv (TLV)"),
        ("BRS", "Bristol (BRS)"),
        ("BGO", "Bergen (BGO)"),
        ("OPO", "Oporto (OPO)"),
        ("LYS", "Lyon (LYS)"),
        ("JFK", "Nueva York (JFK)"),
        ("LAX", "Los Ángeles (LAX)"),
        ("ORD", "Chicago (ORD)"),
        ("MIA", "Miami (MIA)"),
        ("DFW", "Dallas-Fort Worth (DFW)"),
        ("YYZ", "Toronto Pearson (YYZ)"),
        ("LHR", "Londres Heathrow (LHR)"),
        ("SYD", "Sídney (SYD)"),
        ("SIN", "Singapur (SIN)"),
        ("DXB", "Dubái (DXB)"),
        ("ICN", "Seúl (ICN)"),
        ("BKK", "Bangkok (BKK)"),
        ("HND", "Tokio Haneda (HND)"),
        ("PEK", "Pekín (PEK)"),
        ("KUL", "Kuala Lumpur (KUL)"),
        ("MEX", "Ciudad de México (MEX)"),
        ("GRU", "São Paulo (GRU)"),
        ("LIS", "Lisboa (LIS)"),
        ("BOM", "Bombay (BOM)"),
        ("AKL", "Auckland (AKL)"),
        ("CPT", "Ciudad del Cabo (CPT)"),
        ("ZRH", "Zúrich (ZRH)"),
        ("TLV", "Tel Aviv (TLV)"),
        ("JNB", "Johannesburgo (JNB)"),
        ("EZE", "Buenos Aires (EZE)"),
        ("SFO", "San Francisco (SFO)"),
        ("FLL", "Fort Lauderdale (FLL)"),
        ("DEL", "Nueva Delhi (DEL)"),
        ("MUC", "Múnich (MUC)"),
        ("SCL", "Santiago de Chile (SCL)"),
        ("FRA", "Fráncfort (FRA)"),
        ("LHE", "Lahore (LHE)"),
        ("IST", "Estambul (IST)"),
        ("LHR", "Londres Heathrow (LHR)"),
        ("BNE", "Brisbane (BNE)"),
        ("MSP", "Minneapolis (MSP)"),
        ("SEA", "Seattle (SEA)"),
        ("CDG", "París Charles de Gaulle (CDG)"),
        ("CPT", "Ciudad del Cabo (CPT)"),
        ("GRU", "São Paulo (GRU)"),
        ("CMB", "Colombo (CMB)"),
        ("LOS", "Lagos (LOS)"),
        ("YVR", "Vancouver (YVR)"),
        ("LAX", "Los Ángeles (LAX)"),
        ("FCO", "Roma (FCO)")
    ]

    origin = forms.ChoiceField(choices=AIRPORT_CHOICES, label="Origen")
    destination = forms.ChoiceField(choices=AIRPORT_CHOICES, label="Destinació")
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data de sortida")