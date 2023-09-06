import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#TODO: Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_message(headline: str, brief: str):
    account_sid = 'ACeecbfacc5d11ecd74802889f5557d576'
    auth_token = "18cc5ca512054d46d69e4735c69811fd"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+15417033646',
        to='+821088987615',
        body=f"{STOCK}: {emoji}{abs(int(fluctuation))}%\nHeadline:{headline}\nBrief:{brief}"
    )
    print(message.status)


#TODO: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_news(company_name: str):

    day_start = str((datetime.now() - timedelta(4)).date())
    news_params = {
        "q": "Tesla Inc",
        "from": day_start,
        "sortBy": "popularity",
        "language": "en",
        "apiKey": "d42eafcd58a34398a22e8b7ff83eb244"
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_data = news_response.json()["articles"][:3]
    headline_description = {}
    for news in news_data:
        send_message(headline=news["title"], brief=news["description"])

#TODO: When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": "AP1SJYG3MXJTY5G9"
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)

stock_data = response.json()
daily_stock_data = response.json()["Time Series (Daily)"]
yesterday_price = float(list(daily_stock_data.values())[0]["5. adjusted close"])
before_yesterday_price = float(list(daily_stock_data.values())[1]["5. adjusted close"])
fluctuation = (yesterday_price - before_yesterday_price) / 100
emoji = ""
if abs(fluctuation) < 5:
    get_news(COMPANY_NAME)
if fluctuation > 0:
    emoji = "UP"
else:
    emoji = "DOWN"