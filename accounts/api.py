from amadeus import Client
from django.conf import settings
from icecream import ic

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
        ic(response.data)
        return response.data
    except Exception as e:
        ic(e)
        return []
