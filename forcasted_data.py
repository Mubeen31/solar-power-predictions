import requests
import csv
import time

complete_api_link = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/331595?apikey=vnwz1buClrE9YhGJFG3mhNVq23tnIACH&details=true&metric=true'
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data[0])
solar_irradiance_0 = api_data[0]['SolarIrradiance']['Value']
icon_phrase_0 = api_data[0]['IconPhrase']
temperature_0 = api_data[0]['Temperature']['Value']
real_feel_temperature_0 = api_data[0]['RealFeelTemperature']['Value']
dew_point_0 = api_data[0]['DewPoint']['Value']
wind_speed_0 = api_data[0]['Wind']['Speed']['Value']
wind_direction_0 = api_data[0]['Wind']['Direction']['Localized']
humidity_0 = api_data[0]['RelativeHumidity']
visibility_0 = api_data[0]['Visibility']['Value']
uvi_index_0 = api_data[0]['UVIndex']
uvi_index_text_0 = api_data[0]['UVIndexText']
pre_proba_0 = api_data[0]['PrecipitationProbability']
rain_proba_0 = api_data[0]['RainProbability']
cloud_cover_0 = api_data[0]['CloudCover']

solar_irradiance_1 = api_data[1]['SolarIrradiance']['Value']
icon_phrase_1 = api_data[1]['IconPhrase']
temperature_1 = api_data[1]['Temperature']['Value']
real_feel_temperature_1 = api_data[1]['RealFeelTemperature']['Value']
dew_point_1 = api_data[1]['DewPoint']['Value']
wind_speed_1 = api_data[1]['Wind']['Speed']['Value']
wind_direction_1 = api_data[1]['Wind']['Direction']['Localized']
humidity_1 = api_data[1]['RelativeHumidity']
visibility_1 = api_data[1]['Visibility']['Value']
uvi_index_1 = api_data[1]['UVIndex']
uvi_index_text_1 = api_data[1]['UVIndexText']
pre_proba_1 = api_data[1]['PrecipitationProbability']
rain_proba_1 = api_data[1]['RainProbability']
cloud_cover_1 = api_data[1]['CloudCover']

solar_irradiance_2 = api_data[2]['SolarIrradiance']['Value']
icon_phrase_2 = api_data[2]['IconPhrase']
temperature_2 = api_data[2]['Temperature']['Value']
real_feel_temperature_2 = api_data[2]['RealFeelTemperature']['Value']
dew_point_2 = api_data[2]['DewPoint']['Value']
wind_speed_2 = api_data[2]['Wind']['Speed']['Value']
wind_direction_2 = api_data[2]['Wind']['Direction']['Localized']
humidity_2 = api_data[2]['RelativeHumidity']
visibility_2 = api_data[2]['Visibility']['Value']
uvi_index_2 = api_data[2]['UVIndex']
uvi_index_text_2 = api_data[2]['UVIndexText']
pre_proba_2 = api_data[2]['PrecipitationProbability']
rain_proba_2 = api_data[2]['RainProbability']
cloud_cover_2 = api_data[2]['CloudCover']

solar_irradiance_3 = api_data[3]['SolarIrradiance']['Value']
icon_phrase_3 = api_data[3]['IconPhrase']
temperature_3 = api_data[3]['Temperature']['Value']
real_feel_temperature_3 = api_data[3]['RealFeelTemperature']['Value']
dew_point_3 = api_data[3]['DewPoint']['Value']
wind_speed_3 = api_data[3]['Wind']['Speed']['Value']
wind_direction_3 = api_data[3]['Wind']['Direction']['Localized']
humidity_3 = api_data[3]['RelativeHumidity']
visibility_3 = api_data[3]['Visibility']['Value']
uvi_index_3 = api_data[3]['UVIndex']
uvi_index_text_3 = api_data[3]['UVIndexText']
pre_proba_3 = api_data[3]['PrecipitationProbability']
rain_proba_3 = api_data[3]['RainProbability']
cloud_cover_3 = api_data[3]['CloudCover']

solar_irradiance_4 = api_data[4]['SolarIrradiance']['Value']
icon_phrase_4 = api_data[4]['IconPhrase']
temperature_4 = api_data[4]['Temperature']['Value']
real_feel_temperature_4 = api_data[4]['RealFeelTemperature']['Value']
dew_point_4 = api_data[4]['DewPoint']['Value']
wind_speed_4 = api_data[4]['Wind']['Speed']['Value']
wind_direction_4 = api_data[4]['Wind']['Direction']['Localized']
humidity_4 = api_data[4]['RelativeHumidity']
visibility_4 = api_data[4]['Visibility']['Value']
uvi_index_4 = api_data[4]['UVIndex']
uvi_index_text_4 = api_data[4]['UVIndexText']
pre_proba_4 = api_data[4]['PrecipitationProbability']
rain_proba_4 = api_data[4]['RainProbability']
cloud_cover_4 = api_data[4]['CloudCover']

solar_irradiance_5 = api_data[5]['SolarIrradiance']['Value']
icon_phrase_5 = api_data[5]['IconPhrase']
temperature_5 = api_data[5]['Temperature']['Value']
real_feel_temperature_5 = api_data[5]['RealFeelTemperature']['Value']
dew_point_5 = api_data[5]['DewPoint']['Value']
wind_speed_5 = api_data[5]['Wind']['Speed']['Value']
wind_direction_5 = api_data[5]['Wind']['Direction']['Localized']
humidity_5 = api_data[5]['RelativeHumidity']
visibility_5 = api_data[5]['Visibility']['Value']
uvi_index_5 = api_data[5]['UVIndex']
uvi_index_text_5 = api_data[5]['UVIndexText']
pre_proba_5 = api_data[5]['PrecipitationProbability']
rain_proba_5 = api_data[5]['RainProbability']
cloud_cover_5 = api_data[5]['CloudCover']

solar_irradiance_6 = api_data[6]['SolarIrradiance']['Value']
icon_phrase_6 = api_data[6]['IconPhrase']
temperature_6 = api_data[6]['Temperature']['Value']
real_feel_temperature_6 = api_data[6]['RealFeelTemperature']['Value']
dew_point_6 = api_data[6]['DewPoint']['Value']
wind_speed_6 = api_data[6]['Wind']['Speed']['Value']
wind_direction_6 = api_data[6]['Wind']['Direction']['Localized']
humidity_6 = api_data[6]['RelativeHumidity']
visibility_6 = api_data[6]['Visibility']['Value']
uvi_index_6 = api_data[6]['UVIndex']
uvi_index_text_6 = api_data[6]['UVIndexText']
pre_proba_6 = api_data[6]['PrecipitationProbability']
rain_proba_6 = api_data[6]['RainProbability']
cloud_cover_6 = api_data[6]['CloudCover']

solar_irradiance_7 = api_data[7]['SolarIrradiance']['Value']
icon_phrase_7 = api_data[7]['IconPhrase']
temperature_7 = api_data[7]['Temperature']['Value']
real_feel_temperature_7 = api_data[7]['RealFeelTemperature']['Value']
dew_point_7 = api_data[7]['DewPoint']['Value']
wind_speed_7 = api_data[7]['Wind']['Speed']['Value']
wind_direction_7 = api_data[7]['Wind']['Direction']['Localized']
humidity_7 = api_data[7]['RelativeHumidity']
visibility_7 = api_data[7]['Visibility']['Value']
uvi_index_7 = api_data[7]['UVIndex']
uvi_index_text_7 = api_data[7]['UVIndexText']
pre_proba_7 = api_data[7]['PrecipitationProbability']
rain_proba_7 = api_data[7]['RainProbability']
cloud_cover_7 = api_data[7]['CloudCover']

solar_irradiance_8 = api_data[8]['SolarIrradiance']['Value']
icon_phrase_8 = api_data[8]['IconPhrase']
temperature_8 = api_data[8]['Temperature']['Value']
real_feel_temperature_8 = api_data[8]['RealFeelTemperature']['Value']
dew_point_8 = api_data[8]['DewPoint']['Value']
wind_speed_8 = api_data[8]['Wind']['Speed']['Value']
wind_direction_8 = api_data[8]['Wind']['Direction']['Localized']
humidity_8 = api_data[8]['RelativeHumidity']
visibility_8 = api_data[8]['Visibility']['Value']
uvi_index_8 = api_data[8]['UVIndex']
uvi_index_text_8 = api_data[8]['UVIndexText']
pre_proba_8 = api_data[8]['PrecipitationProbability']
rain_proba_8 = api_data[8]['RainProbability']
cloud_cover_8 = api_data[8]['CloudCover']

solar_irradiance_9 = api_data[9]['SolarIrradiance']['Value']
icon_phrase_9 = api_data[9]['IconPhrase']
temperature_9 = api_data[9]['Temperature']['Value']
real_feel_temperature_9 = api_data[9]['RealFeelTemperature']['Value']
dew_point_9 = api_data[9]['DewPoint']['Value']
wind_speed_9 = api_data[9]['Wind']['Speed']['Value']
wind_direction_9 = api_data[9]['Wind']['Direction']['Localized']
humidity_9 = api_data[9]['RelativeHumidity']
visibility_9 = api_data[9]['Visibility']['Value']
uvi_index_9 = api_data[9]['UVIndex']
uvi_index_text_9 = api_data[9]['UVIndexText']
pre_proba_9 = api_data[9]['PrecipitationProbability']
rain_proba_9 = api_data[9]['RainProbability']
cloud_cover_9 = api_data[9]['CloudCover']

solar_irradiance_10 = api_data[10]['SolarIrradiance']['Value']
icon_phrase_10 = api_data[10]['IconPhrase']
temperature_10 = api_data[10]['Temperature']['Value']
real_feel_temperature_10 = api_data[10]['RealFeelTemperature']['Value']
dew_point_10 = api_data[10]['DewPoint']['Value']
wind_speed_10 = api_data[10]['Wind']['Speed']['Value']
wind_direction_10 = api_data[10]['Wind']['Direction']['Localized']
humidity_10 = api_data[10]['RelativeHumidity']
visibility_10 = api_data[10]['Visibility']['Value']
uvi_index_10 = api_data[10]['UVIndex']
uvi_index_text_10 = api_data[10]['UVIndexText']
pre_proba_10 = api_data[10]['PrecipitationProbability']
rain_proba_10 = api_data[10]['RainProbability']
cloud_cover_10 = api_data[10]['CloudCover']

solar_irradiance_11 = api_data[11]['SolarIrradiance']['Value']
icon_phrase_11 = api_data[11]['IconPhrase']
temperature_11 = api_data[11]['Temperature']['Value']
real_feel_temperature_11 = api_data[11]['RealFeelTemperature']['Value']
dew_point_11 = api_data[11]['DewPoint']['Value']
wind_speed_11 = api_data[11]['Wind']['Speed']['Value']
wind_direction_11 = api_data[11]['Wind']['Direction']['Localized']
humidity_11 = api_data[11]['RelativeHumidity']
visibility_11 = api_data[11]['Visibility']['Value']
uvi_index_11 = api_data[11]['UVIndex']
uvi_index_text_11 = api_data[11]['UVIndexText']
pre_proba_11 = api_data[11]['PrecipitationProbability']
rain_proba_11 = api_data[11]['RainProbability']
cloud_cover_11 = api_data[11]['CloudCover']


with open("hourly_weather_forecasted_data.csv", "a", newline = '\n') as f:
    writer = csv.writer(f, delimiter = ",")
    writer.writerow(
        [solar_irradiance_0, icon_phrase_0, temperature_0, real_feel_temperature_0, dew_point_0, wind_speed_0,
         wind_direction_0, humidity_0, visibility_0, uvi_index_0, uvi_index_text_0, pre_proba_0, rain_proba_0,
         cloud_cover_0])
    writer.writerow(
        [solar_irradiance_1, icon_phrase_1, temperature_1, real_feel_temperature_1, dew_point_1, wind_speed_1,
         wind_direction_1, humidity_1, visibility_1, uvi_index_1, uvi_index_text_1, pre_proba_1, rain_proba_1,
         cloud_cover_1])
    writer.writerow(
        [solar_irradiance_2, icon_phrase_2, temperature_2, real_feel_temperature_2, dew_point_2, wind_speed_2,
         wind_direction_2, humidity_2, visibility_2, uvi_index_2, uvi_index_text_2, pre_proba_2, rain_proba_2,
         cloud_cover_2])
    writer.writerow(
        [solar_irradiance_3, icon_phrase_3, temperature_3, real_feel_temperature_3, dew_point_3, wind_speed_3,
         wind_direction_3, humidity_3, visibility_3, uvi_index_3, uvi_index_text_3, pre_proba_3, rain_proba_3,
         cloud_cover_3])
    writer.writerow(
        [solar_irradiance_4, icon_phrase_4, temperature_4, real_feel_temperature_4, dew_point_4, wind_speed_4,
         wind_direction_4, humidity_4, visibility_4, uvi_index_4, uvi_index_text_4, pre_proba_4, rain_proba_4,
         cloud_cover_4])
    writer.writerow(
        [solar_irradiance_5, icon_phrase_5, temperature_5, real_feel_temperature_5, dew_point_5, wind_speed_5,
         wind_direction_5, humidity_5, visibility_5, uvi_index_5, uvi_index_text_5, pre_proba_5, rain_proba_5,
         cloud_cover_5])
    writer.writerow(
        [solar_irradiance_6, icon_phrase_6, temperature_6, real_feel_temperature_6, dew_point_6, wind_speed_6,
         wind_direction_6, humidity_6, visibility_6, uvi_index_6, uvi_index_text_6, pre_proba_6, rain_proba_6,
         cloud_cover_6])
    writer.writerow(
        [solar_irradiance_7, icon_phrase_7, temperature_7, real_feel_temperature_7, dew_point_7, wind_speed_7,
         wind_direction_7, humidity_7, visibility_7, uvi_index_7, uvi_index_text_7, pre_proba_7, rain_proba_7,
         cloud_cover_7])
    writer.writerow(
        [solar_irradiance_8, icon_phrase_8, temperature_8, real_feel_temperature_8, dew_point_8, wind_speed_8,
         wind_direction_8, humidity_8, visibility_8, uvi_index_8, uvi_index_text_8, pre_proba_8, rain_proba_8,
         cloud_cover_8])
    writer.writerow(
        [solar_irradiance_9, icon_phrase_9, temperature_9, real_feel_temperature_9, dew_point_9, wind_speed_9,
         wind_direction_9, humidity_9, visibility_9, uvi_index_9, uvi_index_text_9, pre_proba_9, rain_proba_9,
         cloud_cover_9])
    writer.writerow(
        [solar_irradiance_10, icon_phrase_10, temperature_10, real_feel_temperature_10, dew_point_10, wind_speed_10,
         wind_direction_10, humidity_10, visibility_10, uvi_index_10, uvi_index_text_10, pre_proba_10, rain_proba_10,
         cloud_cover_10])
    writer.writerow(
        [solar_irradiance_11, icon_phrase_11, temperature_11, real_feel_temperature_11, dew_point_11, wind_speed_11,
         wind_direction_11, humidity_11, visibility_11, uvi_index_11, uvi_index_text_11, pre_proba_11, rain_proba_11,
         cloud_cover_11])
