# This class is responsible for talking to the Flight Search API.
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

API_KEY = "1E2jKuUDkAlXcHlqQ_Xzwn0zFrVcPRrq"
tequila_endpoint = "https://api.tequila.kiwi.com/"
headers = {"apikey": API_KEY}
location_params = {"location_types": "city",}


class FlightSearch:

    def find_iata(self, cities: list):
        self.iatas = []
        for city in cities:
            location_params["term"] = city
            response = requests.get(url=tequila_endpoint + "locations/query", headers=headers,
                                    params=location_params)
            self.iatas.append(response.json()["locations"][0]["code"])
        return self.iatas

    def check_flight(self, fly_from: str, fly_to: str, price_to: int):
        params = {
            "fly_to": fly_to,
            "price_to": price_to,
            "fly_from": fly_from,
            "date_from": datetime.now().date().strftime("%d/%m/%Y"),
            "date_to": (datetime.now().date() + relativedelta(months=+6)).strftime("%d/%m/%Y"),
            "adults": 1,
            "selected_cabins": "M",
            "max_stopovers": 0
        }
        response = requests.get(url=tequila_endpoint + "v2/search", headers=headers, params=params)
        data = response.json()["data"]

        if self.data:
            city_from = self.data[0]["cityFrom"]
            city_to = self.data[0]["cityTo"]
            # price = []
            # date_list = []
            # self.date_list_final = []
            # for data in self.data:
            #     if data["fare"]["adults"] <= price_to:
            #         self.price.append(data["fare"]["adults"])
            #         self.date_list.append(data["route"][0]["local_departure"][:10])
            # if self.price.count(min(self.price)) == 1:
            #     self.price = self.price[0]
            #     self.date_list_final = [self.date_list[0]]
            # else:
            #     idx_list = list(filter(lambda x: self.price[x] == min(self.price), range(len(self.price))))
            #     self.price = self.price[idx_list[0]]
            #     for idx in idx_list:
            #         self.date_list_final.append(self.date_list[idx])

        # else:
            # print(f"{self.fly_to}로 가는 조건을 만족하는 티켓이 없습니다.")

# dict = {'PAR': 54, 'BER': 42, 'TYO': 485, 'SYD': 551, 'IST': 95, 'KUL': 414, 'NYC': 240, 'SFO': 260, 'CPT': 378}
# for key, value in dict.items():
#     flight = FlightSearch(fly_to=key, price_to=value)
#     try:
#         print(key)
#         print(flight.data)
#         print(flight.price)
#         print(flight.date_list)
#         print(flight.date_list_final)
#         print("-----------------------------------")
#     except:
#         pass
