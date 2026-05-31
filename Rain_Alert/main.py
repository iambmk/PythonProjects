import requests
import os
from twilio.rest import Client
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")  #twilio_auth_token
weather_params = {
    "lat": 17.800659,
    "lon": 79.009851,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body="It's going to rain today. Remember to bring ☂️",
        from_="+14243527208",
        to='+917893449664',
    )
print(message.status)