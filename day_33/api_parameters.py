import requests
from datetime import datetime

MY_LAT = 37.532600
MY_LONG = 127.024612

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status() # EXCEPTION
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

time_now = datetime.now()
time_now.hour