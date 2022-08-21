import requests
from datetime import datetime
import os
from twilio.rest import Client

current_endpoint= "https://api.openweathermap.org/data/2.5/weather?"
forecast_endpoint= "https://api.openweathermap.org/data/2.5/forecast?"
current_weather_params= {
    "lat": -37.83754046057603,
    "lon": 145.18570321833164,
    "appid": os.environ.get('OWM_API_KEY'),
    "units": "metric"
}
forecast_weather_params= {
    "lat": -37.83754046057603,
    "lon": 145.18570321833164,
    "appid": os.environ.get('OWM_API_KEY'),
    "units": "metric",
    "cnt": 1
}
data=requests.get(forecast_endpoint, params= forecast_weather_params).json()
forecast_time= datetime.fromtimestamp(data["list"][0]["dt"])
forecast_temp=data["list"][0]["main"]["temp"]
forecast_descript = data["list"][0]["weather"][0]["description"]
print(forecast_time,"the weather is:",forecast_descript,".the temp will be:", forecast_temp)

message_body ="The weather will be:"+forecast_descript+". The temp will be: "+str(forecast_temp)+("C at ") +str(forecast_time)
print(message_body)

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body= message_body,
         from_='+13253357279',
         to='your number'
     )

print(message.sid)