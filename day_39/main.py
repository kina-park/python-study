#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

tequila_endpoint = "https://api.tequila.kiwi.com/"
API_KEY = "1E2jKuUDkAlXcHlqQ_Xzwn0zFrVcPRrq"
headers = {
    "apikey": API_KEY
}
location_params = {
    "location_types": "city"
}
data_manager = DataManager()
cities = data_manager.get_cities()

iatas = []  # ['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT']
for city in cities:
    location_params["term"] = city
    response = requests.get(url=tequila_endpoint+"locations/query", headers=headers, params=location_params)
    iatas.append(response.json()["locations"][0]["code"])

data_manager.add_IATA(iata_list=iatas)
# data_manager.iatas_prices = {'PAR': 54, 'BER': 42, 'TYO': 485, 'SYD': 551, 'IST': 95, 'KUL': 414, 'NYC': 240, 'SFO': 260, 'CPT': 378}

flight_search_obj_list = []
for iata, price in data_manager.iatas_prices.items():
    flight_search = FlightSearch(fly_to=iata, price_to=price)
    flight_search_obj_list.append(flight_search)

max_price = max([value for value in data_manager.iatas_prices.values()])
flight_data = FlightData(flight_search_obj_list=flight_search_obj_list, max_price=max_price)
notification = NotificationManager(
    messasge=f"Low price alert! Only £{flight_data.lowest_price} to fly from {flight_data.city_from}-"
             f"{flight_data.fly_from} to {flight_data.city_to}-{flight_data.fly_to} on {flight_data.flight_date}"
)
