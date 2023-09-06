# TODO. 1: (알아두기!) str -> datetime
# from datetime import datetime
# date_strings = ['2023-11-18', '2024-01-05', '2023-10-11', '2024-01-07', '2023-09-26', '2023-09-26']
# date_objects = sorted([datetime.strptime(date_str, '%Y-%m-%d').date() for date_str in date_strings])
# print(date_objects)

# TODO. 2: (알아두기!) 데이터 깔끔하게 출력하기
# from pprint import pprint
# pprint()

# TODO. 3: (알아두기!) 특정 값에 해당하는 모든 인덱스를 리스트로 만들기
# li = [1, 1, 2, 3, 4, 4, 6, 7, 7, 1, 8]
# idx_list = list(filter(lambda x: li[x] == min(li), range(len(li))))

# TODO. 4: (알아두기!) 인덱스로 리스트 원소 삭제하기
# li = [1, 1, 2, 3, 4, 4, 6, 7, 7, 1, 8]
# del li(9) - > li = [1, 1, 2, 3, 4, 4, 6, 7, 7, 8]

import requests
from pprint import pprint
sheety_endpoint = "https://api.sheety.co/33cc0b98c5718b7e24cc45e0590e8808/flightDealsCopy/prices"

response = requests.get(url=sheety_endpoint)
data = response.json()["prices"]
cities = [row["city"] for row in data]
print(cities)
# ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
# [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
#  {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
#  {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485}, ...

tequila_endpoint = "https://api.tequila.kiwi.com/"
API_KEY = "1E2jKuUDkAlXcHlqQ_Xzwn0zFrVcPRrq"
headers = {
    "apikey": API_KEY
}
location_params = {
    "location_types": "city"
}
cities = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']
iatas = []
for city in cities:
    location_params["term"] = city
    response = requests.get(url=tequila_endpoint+"locations/query", headers=headers, params=location_params)
    iatas.append(response.json()["locations"][0]["code"])
print(iatas)