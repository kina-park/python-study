from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# TODO 1: 구글 시트 IATA CODE 업데이트
data_manager = DataManager()
flight_search = FlightSearch()
cities = data_manager.get_cities()
iatas = flight_search.find_iata(cities=cities)
data_manager.update_iata_code(iata_list=iatas)

# flight_check_obj_list = []
# for iata, price in data_manager.iatas_prices.items():
#     flight_check = FlightSearch(fly_to=iata, price_to=price)
#     flight_check_obj_list.append(flight_search)
#
# max_price = max([value for value in data_manager.iatas_prices.values()])
# flight_data = FlightData(flight_search_obj_list=flight_search_obj_list, max_price=max_price)
# notification = NotificationManager(
#     messasge=f"Low price alert! Only £{flight_data.lowest_price} to fly from {flight_data.city_from}-"
#              f"{flight_data.fly_from} to {flight_data.city_to}-{flight_data.fly_to} on {flight_data.flight_date}"
# )