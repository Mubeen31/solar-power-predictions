import requests
import csv
import time
from datetime import datetime

complete_api_link = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/331595?apikey=vnwz1buClrE9YhGJFG3mhNVq23tnIACH&details=true&metric=true'
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data['DailyForecasts'][0])

date_time_0 = api_data['DailyForecasts'][0]['Date']
get_date_time = datetime.strptime(date_time_0, '%Y-%m-%dT%H:%M:%S%z')
dte_0 = get_date_time.strftime('%Y-%m-%d')
solar_irradiance_0 = api_data['DailyForecasts'][0]['Day']['SolarIrradiance']['Value']
temp_min_0 = api_data['DailyForecasts'][0]['Temperature']['Minimum']['Value']
temp_max_0 = api_data['DailyForecasts'][0]['Temperature']['Maximum']['Value']
weather_status_0 = api_data['DailyForecasts'][0]['Day']['IconPhrase']
cloud_cover_0 = api_data['DailyForecasts'][0]['Day']['CloudCover']

date_time_1 = api_data['DailyForecasts'][1]['Date']
get_date_time = datetime.strptime(date_time_1, '%Y-%m-%dT%H:%M:%S%z')
dte_1 = get_date_time.strftime('%Y-%m-%d')
solar_irradiance_1 = api_data['DailyForecasts'][1]['Day']['SolarIrradiance']['Value']
temp_min_1 = api_data['DailyForecasts'][1]['Temperature']['Minimum']['Value']
temp_max_1 = api_data['DailyForecasts'][1]['Temperature']['Maximum']['Value']
weather_status_1 = api_data['DailyForecasts'][1]['Day']['IconPhrase']
cloud_cover_1 = api_data['DailyForecasts'][1]['Day']['CloudCover']

date_time_2 = api_data['DailyForecasts'][2]['Date']
get_date_time = datetime.strptime(date_time_2, '%Y-%m-%dT%H:%M:%S%z')
dte_2 = get_date_time.strftime('%Y-%m-%d')
solar_irradiance_2 = api_data['DailyForecasts'][2]['Day']['SolarIrradiance']['Value']
temp_min_2 = api_data['DailyForecasts'][2]['Temperature']['Minimum']['Value']
temp_max_2 = api_data['DailyForecasts'][2]['Temperature']['Maximum']['Value']
weather_status_2 = api_data['DailyForecasts'][2]['Day']['IconPhrase']
cloud_cover_2 = api_data['DailyForecasts'][2]['Day']['CloudCover']

date_time_3 = api_data['DailyForecasts'][3]['Date']
get_date_time = datetime.strptime(date_time_3, '%Y-%m-%dT%H:%M:%S%z')
dte_3 = get_date_time.strftime('%Y-%m-%d')
solar_irradiance_3 = api_data['DailyForecasts'][3]['Day']['SolarIrradiance']['Value']
temp_min_3 = api_data['DailyForecasts'][3]['Temperature']['Minimum']['Value']
temp_max_3 = api_data['DailyForecasts'][3]['Temperature']['Maximum']['Value']
weather_status_3 = api_data['DailyForecasts'][3]['Day']['IconPhrase']
cloud_cover_3 = api_data['DailyForecasts'][3]['Day']['CloudCover']

date_time_4 = api_data['DailyForecasts'][4]['Date']
get_date_time = datetime.strptime(date_time_4, '%Y-%m-%dT%H:%M:%S%z')
dte_4 = get_date_time.strftime('%Y-%m-%d')
solar_irradiance_4 = api_data['DailyForecasts'][4]['Day']['SolarIrradiance']['Value']
temp_min_4 = api_data['DailyForecasts'][4]['Temperature']['Minimum']['Value']
temp_max_4 = api_data['DailyForecasts'][4]['Temperature']['Maximum']['Value']
weather_status_4 = api_data['DailyForecasts'][4]['Day']['IconPhrase']
cloud_cover_4 = api_data['DailyForecasts'][4]['Day']['CloudCover']

with open("daily_weather_forecasted_data.csv", "a", newline = '\n') as f:
    writer = csv.writer(f, delimiter = ",")
    writer.writerow([dte_0, solar_irradiance_0, temp_min_0, temp_max_0, weather_status_0, cloud_cover_0])
    writer.writerow([dte_1, solar_irradiance_1, temp_min_1, temp_max_1, weather_status_1, cloud_cover_1])
    writer.writerow([dte_2, solar_irradiance_2, temp_min_2, temp_max_2, weather_status_2, cloud_cover_2])
    writer.writerow([dte_3, solar_irradiance_3, temp_min_3, temp_max_3, weather_status_3, cloud_cover_3])
    writer.writerow([dte_4, solar_irradiance_4, temp_min_4, temp_max_4, weather_status_4, cloud_cover_4])
