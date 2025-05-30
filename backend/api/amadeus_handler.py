import os
from amadeus import Client, ResponseError, Location
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


class AmadeusHandler:
    def __init__(self):
        self.am_client_id:str = os.getenv("AMADEUS_API")
        self.am_client_secret:str = os.getenv("AMADEUS_SECRET")
        self.client = Client(client_id=self.am_client_id,
                             client_secret=self.am_client_secret)

        #self.client.next(response)  # => returns a new response for the next page

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
        # testing = api.client.reference_data.locations.get(keyword='LON',
        #                                                   subType=Location.AIRPORT)
        # testing = api.client.shopping.flight_destinations.get(origin='MAD')
        params = {"originCityCode": "MAD",
                  "period": "2017-01",
                  "max": 50,
                  "page[limit]": 50}
        testing = api.get_any("/v1/travel/analytics/air-traffic/traveled", **params)
        print(testing)
        # data = testing.data
        # df = pd.DataFrame(testing)
        # df.to_csv("test_flights_most_traveled.csv", index=False)
        # print(df)