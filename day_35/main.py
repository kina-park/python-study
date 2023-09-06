import requests
from twilio.rest import Client
import os
#######################################################################################################################

# http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
OWM_Endpoint ="https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY")  ### 환경 변수 설정:  Run > Edit Configurations

weather_params = {
    "lat": "36.27",
    "lon": "111.48",
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

account_sid = 'ACeecbfacc5d11ecd74802889f5557d576'
auth_token = os.environ.get("AUTH_TOKEN")   ### 환경 변수 설정:  Run > Edit Configurations
#######################################################################################################################

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+15417033646',
        to='+821088987615',
        body="It's going to rain today. Remember to bring an umbrella.☂️"
    )
    print(message.status)

