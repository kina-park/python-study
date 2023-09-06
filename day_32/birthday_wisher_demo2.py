import pandas as pd
from datetime import datetime
import random
import smtplib

MY_EMAIL = "qkrrlsk8062@gmail.com"
MY_PASSWORD = "mgwewjxekprnswtv"

today = datetime.now()
today_tuple = (datetime.now().month, datetime.now().day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_peron = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, "r") as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_peron["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_peron["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
