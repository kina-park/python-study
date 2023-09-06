import requests
from datetime import datetime
import os

APP_ID = os.environ.get("NT_APP_ID")  # 환경변수를 가져오는 방법
APP_KEY = os.environ.get("NT_APP_KEY")

GENDER = "female"
WEIGHT_KG = 50
HEIGHT_CM = 163
AGE = 29
exercise_text = input("Tell me which exercises you did: ")

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": os.environ.get("NT_APP_ID"),
    "x-app-key": os.environ.get("NT_APP_KEY"),
    "x-remote-user-id": "0"
}
parameters = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

response = requests.post(url=end_point, headers=headers, json=parameters)
data = response.json()["exercises"]
print(response.status_code)
print(response.text)
duration = data[0]["duration_min"]
calories = data[0]["nf_calories"]
exercise = data[0]["name"]

#####################################################################################
sheety_endpoint = "https://api.sheety.co/bf921784c8b5ebc22011f5bdcf4834cc/workoutTracking/workouts"
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%T")
TOKEN = os.environ.get("NT_TOKEN")
workouts = {
    "workout":
        {
            "date": date,
            "time": time,
            "exercise": exercise.capitalize(),
            "duration": duration,
            "calories": calories
        }
    }
header = {
    "Authorization": f"Basic {TOKEN}"
}
response = requests.post(url=sheety_endpoint, json=workouts, headers=header)
print(response.status_code)
print(response.text)

