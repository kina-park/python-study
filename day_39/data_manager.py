# This class is responsible for talking to the Google Sheet.

import requests

sheety_endpoint = "https://api.sheety.co/33cc0b98c5718b7e24cc45e0590e8808/flightDealsCopy/prices"


class DataManager:
    def __init__(self):
        self.iatas_prices = []

    def get_cities(self):
        self.response = requests.get(url=sheety_endpoint)
        self.data = self.response.json()["prices"]
        self.cities = [iter["city"] for iter in self.data]
        return self.cities

    def update_iata_code(self, iata_list: list, object_id=2):
        for iata in iata_list:
            data = {
                "price": {
                    "iataCode": iata
                }
            }
            self.response = requests.put(url=sheety_endpoint+"/"+f"{object_id}", json=data)
            object_id += 1
        self.iatas_prices = {iter["iataCode"]: iter["lowestPrice"]
                             for iter in requests.get(url=sheety_endpoint).json()["prices"]}


