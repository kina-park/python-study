import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "AP1SJYG3MXJTY5G9"
NEWS_API_KEY = "d42eafcd58a34398a22e8b7ff83eb244"
TWILIO_SID = 'ACeecbfacc5d11ecd74802889f5557d576'
TWILIO_AUTH_TOKEN = "18cc5ca512054d46d69e4735c69811fd"

######################################################################################

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]
yesterday_closing_price = float(yesterday_data["5. adjusted close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["5. adjusted close"])
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "UP"
else:
    up_down = "DOWN"
diff_percent = round((difference / yesterday_closing_price) * 100)

if abs(diff_percent) > 5:

    news_params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]

    for formatted_article in formatted_articles:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_='+15417033646',
            to='+821088987615',
            body=formatted_article
        )
