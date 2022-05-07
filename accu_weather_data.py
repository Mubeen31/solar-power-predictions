import requests
import csv
import time
from datetime import datetime

i = 1
while i == 1:
    complete_api_link = 'http://dataservice.accuweather.com/currentconditions/v1/331595?apikey=vnwz1buClrE9YhGJFG3mhNVq23tnIACH&details=true'
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    weather_status = api_data[0]['WeatherText']
    temp = api_data[0]['Temperature']['Metric']['Value']
    real_feel_temp = api_data[0]['RealFeelTemperature']['Metric']['Value']
    hum = api_data[0]['RelativeHumidity']
    dew_point = api_data[0]['DewPoint']['Metric']['Value']
    wind_direction = api_data[0]['Wind']['Direction']['Localized']
    wind_speed = api_data[0]['Wind']['Speed']['Metric']['Value']
    visi = api_data[0]['Visibility']['Metric']['Value']
    press = api_data[0]['Pressure']['Metric']['Value']
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    time.sleep(60)
    with open("accu_weather_data.csv", "a", newline = '\n') as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, weather_status, temp, real_feel_temp, hum, dew_point, wind_direction, wind_speed,
                         visi, press])
        print(dt_string, weather_status, temp, real_feel_temp, hum, dew_point, wind_direction, wind_speed, visi, press)
