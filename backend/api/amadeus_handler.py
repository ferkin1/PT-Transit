import os
from amadeus import Client, ResponseError, Location
import requests
from dotenv import load_dotenv

load_dotenv()


class AmadeusHandler:

    def __init__(self):
        self.am_client_id = os.getenv("AMADEUS_API")
        self.am_client_secret = os.getenv("AMADEUS_SECRET")
        self.client = Client(client_id=self.am_client_id,
                             client_secret=self.am_client_secret)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"[AmadeusHandler] Exited with error: {exc_val}")

    def get_any(self, endpoint:str, **params):
        try:
            response = self.client.get(endpoint, **params)
            return response.data
        except ResponseError as e:
            print(f"[GET] Error: {e}")
            return []

    def get_popular_destinations(self, origin, max_price=1000):
        try:
            return self.client.shopping.flight_destinations.get(origin=origin,
                                                                maxPrice=max_price).data
        except ResponseError as e:
            print(f"An error occurred: {e}")
            return []


if __name__ == "__main__":
    with AmadeusHandler() as api:
        testing = api.client.reference_data.locations.get(keyword='LON',
                                                          subType=Location.AIRPORT)

    print(testing.data)