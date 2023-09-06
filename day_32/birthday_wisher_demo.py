##################### Extra Hard Starting Project ######################

# TODO:1. Update the birthdays.csv
# TODO:2. Check if today matches a birthday in the birthdays.csv
# TODO:3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# TODO:4. Send the letter generated in step 3 to that person's email address.

from datetime import datetime
import pandas as pd
import random
import os
import smtplib

month = datetime.now().month
day = datetime.now().day

df = pd.read_csv("birthdays.csv")
birthday_list = df.to_dict(orient="records")
letter = random.choice(os.listdir("letter_templates/"))


def customize_letter(new_str, file_path=f"letter_templates/{letter}", old_str="[NAME]"):
    with open(file_path, 'r') as f:
        lines = f.read()
    lines = lines.replace("[NAME]", new_str)
    return lines


for birthday in birthday_list:
    if (birthday["month"] == month) & (birthday["day"] == day):
        letter_body = customize_letter(new_str=birthday["name"])
        my_email = "qkrrlsk8062@gmail.com"
        password = "mgwewjxekprnswtv"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_body}")