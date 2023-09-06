# Application Programming Interfaces (API)
# API는 일련의 명령, 함수, 프로토콜, 객체로 구성되어 있음.
# 프로그래머는 API를 이용해서 소프트웨어를 생성하거나 외부 시스템과 상호작용할 수 있음.
# 즉, 다양한 웹사이트와 상호작용 함으로써, 웹사이트에서 라이브 데이터를 가져올 것임
# Request, Response 과정을 통해 데이터를 가져오기

# API 엔드포인트

import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")  # 엔드포인트 url으로부터 데이터를 얻도록 도와줌
# print(response.raise_for_status())
# print(response.status_code)
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")
# 응답코드 종류 (HTTP Status Code)
# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You ScrewedUp
# 5XX: I Screwed U

data = response.json()
# data = response.json().["iss_position"]
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

