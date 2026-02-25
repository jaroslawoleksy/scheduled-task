import datetime as dt
import random
import pandas
import smtplib
import os
##################### Extra Hard Starting Project ######################

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
birthdays=[]

def send_email(address, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=address,
            msg=f"Subject:Happy Birthday!\n\n{message}"
        )

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
try:
    with open("birthdays.csv", "r") as birthdays_data:
        birthdays_list = pandas.read_csv(birthdays_data)
except FileNotFoundError:
    print("No data file")
else:
    birthdays = birthdays_list.to_dict("records")
    print(birthdays)

now = dt.datetime.now()
current_month = now.month
current_day = now.day
for person in birthdays:
    if person["month"] == current_month and person["day"] == current_day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_file = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_file) as letter_template:
            starting_letter = letter_template.read()
            letter_to_send = starting_letter.replace("[NAME]", person["name"])
            print(letter_to_send)
# 4. Send the letter generated in step 3 to that person's email address.
            send_email(person["email"], letter_to_send)



