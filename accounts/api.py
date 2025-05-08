
from amadeus import Client
from django.conf import settings

amadeus = Client(
    client_id=settings.AMADEUS_CLIENT['client_id'],
    client_secret=settings.AMADEUS_CLIENT['client_secret']
)

def search_flights(origin, destination, departure_date):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            adults=1
        )
        return response.data  # Retorna les dades dels vols
    except Exception as e:
        print(f"Error en l'API: {e}")
        return []