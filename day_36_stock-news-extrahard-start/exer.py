from datetime import datetime, timedelta
import requests
# print(str(dt.datetime.now().date()))

day_from = str((datetime.now() - timedelta(4)).date())
# print(day_from)
# today = str(dt.datetime.now().date())
#
news_params = {
    "q": "Tesla Inc",
    "from": day_from,
    "sortBy": "popularity",
    "language": "en",
    "apiKey":"d42eafcd58a34398a22e8b7ff83eb244"
}
response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
print(response.json()["articles"][:3])