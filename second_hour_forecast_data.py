import requests
import csv
import time

i = 1
while i == 1:
    complete_api_link = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/331595?apikey=vnwz1buClrE9YhGJFG3mhNVq23tnIACH&details=true&metric=true'
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    date_time = api_data[1]['DateTime']
    icon = api_data[1]['IconPhrase']
    temp = api_data[1]['Temperature']['Value']
    real_feel_temp = api_data[1]['RealFeelTemperature']['Value']
    pre = api_data[1]['PrecipitationProbability']
    time.sleep(240)
    with open("second_hour_forecast_data.csv", "a", newline = '\n') as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([date_time, icon, temp, real_feel_temp, pre])
        print(date_time, icon, temp, real_feel_temp, pre)
