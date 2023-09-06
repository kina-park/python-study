# This class is responsible for structuring the flight data.
from datetime import datetime


class FlightData:

    def __init__(self, flight_search_obj_list: list, max_price: int):
        for flight_search in flight_search_obj_list:
            if flight_search.data:
                if flight_search.price:
                    if flight_search.price < max_price:
                        self.lowest_price = flight_search.price
                        self.city_from = flight_search.city_from
                        self.fly_from = flight_search.fly_from
                        self.city_to = flight_search.city_to
                        self.fly_to = flight_search.fly_to
                        self.flight_date = sorted([datetime.strptime(date_str, '%Y-%m-%d').date() for date_str in flight_search.date_list_final])

        # if self.flight_date_str:
        #     if len(self.flight_date_str) == 1:
        #         print(f"the_lowest_price: {self.lowest_price}euro, city_from: {self.city_from}, fly_from: {self.fly_from}, city_to: {self.city_to}, fly_to:{self.fly_to}, flight_date: {self.flight_date}")
        #     else:
        #         self.flight_date = sorted([datetime.strptime(date_str, '%Y-%m-%d').date() for date_str in self.flight_date_str])
        #         print(f"the_lowest_price: {self.lowest_price}euro, city_from: {self.city_from}, fly_from: {self.fly_from}, city_to: {self.city_to}, fly_to:{self.fly_to}, from {self.flight_date[0]}-{self.flight_date[-1]}")
