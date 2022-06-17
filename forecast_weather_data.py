import requests
import csv
import time

# i = 1
# while i == 1:
complete_api_link = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/331595?apikey=vnwz1buClrE9YhGJFG3mhNVq23tnIACH&details=true&metric=true'
api_link = requests.get(complete_api_link)
api_data = api_link.json()
date_time_0 = api_data[0]['DateTime']
icon_0 = api_data[0]['IconPhrase']
temp_0 = api_data[0]['Temperature']['Value']
real_feel_temp_0 = api_data[0]['RealFeelTemperature']['Value']
pre_0 = api_data[0]['PrecipitationProbability']
date_time_1 = api_data[1]['DateTime']
icon_1 = api_data[1]['IconPhrase']
temp_1 = api_data[1]['Temperature']['Value']
real_feel_temp_1 = api_data[1]['RealFeelTemperature']['Value']
pre_1 = api_data[1]['PrecipitationProbability']
date_time_2 = api_data[2]['DateTime']
icon_2 = api_data[2]['IconPhrase']
temp_2 = api_data[2]['Temperature']['Value']
real_feel_temp_2 = api_data[2]['RealFeelTemperature']['Value']
pre_2 = api_data[2]['PrecipitationProbability']
# time.sleep(240)
# with open("forecast_weather_data.csv", "a", newline = '\n') as f:
#     writer = csv.writer(f, delimiter = ",")
#     writer.writerow([date_time_0, icon_0, temp_0, real_feel_temp_0, pre_0])
#     writer.writerow([date_time_1, icon_1, temp_1, real_feel_temp_1, pre_1])
#     writer.writerow([date_time_2, icon_2, temp_2, real_feel_temp_2, pre_2])
print(date_time_0, icon_0, temp_0, real_feel_temp_0, pre_0)
print(date_time_1, icon_1, temp_1, real_feel_temp_1, pre_1)
print(date_time_2, icon_2, temp_2, real_feel_temp_2, pre_2)
