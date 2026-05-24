import smtplib
import datetime as dt
import random

my_email = "mohanbaratam@gmail.com"
password = "fgunpihhvmfbrxqw"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation!\n\n{quote}"
                            )
