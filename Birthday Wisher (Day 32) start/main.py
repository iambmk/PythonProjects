# import smtplib
#
#
# my_email = "mohanbaratam@gmail.com"
# password = "fgunpihhvmfbrxqw"
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="baratammohankrishna1@gmail.com",
#                         msg="Subject:hello\n\nThis is the body of email."
#                         )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
