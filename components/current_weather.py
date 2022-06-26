import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
from datetime import datetime, date, time
from datetime import timedelta
from sklearn import linear_model
import sqlalchemy
from dash import dash_table as dt
import time
import requests

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

html.Div([
    dcc.Interval(id = 'update_date_time_value',
                 interval = 60000,
                 n_intervals = 0),
]),


def current_weather_value(n_intervals):
    # header_list = ['Date Time', 'Weather Status', 'Temperature', 'Real Feel Temperature', 'Humidity', 'Dew Point',
    #                'Wind Direction', 'Wind Speed', 'Visibility', 'Pressure']
    # df = pd.read_csv('accu_weather_data.csv', names = header_list)
    # weather_status = df['Weather Status'].tail(1).iloc[0]
    # temp = df['Temperature'].tail(1).iloc[0]
    # feels_like_temp = df['Real Feel Temperature'].tail(1).iloc[0]
    # wind_speed = df['Wind Speed'].tail(1).iloc[0]
    # wind_direction = df['Wind Direction'].tail(1).iloc[0]
    # hum = df['Humidity'].tail(1).iloc[0]
    # pr = df['Pressure'].tail(1).iloc[0]
    # dew_point = df['Dew Point'].tail(1).iloc[0]
    # vs = df['Visibility'].tail(1).iloc[0]
    sun_complete_api_link = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/331595?apikey=vnwz1buClrE9YhGJFG3mhNVq23tnIACH&details=true&metric=true'
    sun_api_link = requests.get(sun_complete_api_link)
    sun_api_data = sun_api_link.json()
    sun_rise = sun_api_data['DailyForecasts'][0]['Sun']['Rise']
    rise_date_time = datetime.strptime(sun_rise, '%Y-%m-%dT%H:%M:%S%z')
    sun_rise_time = rise_date_time.strftime('%H:%M')
    sun_set = sun_api_data['DailyForecasts'][0]['Sun']['Set']
    set_date_time = datetime.strptime(sun_set, '%Y-%m-%dT%H:%M:%S%z')
    sun_set_time = set_date_time.strftime('%H:%M')
    complete_api_link = 'http://dataservice.accuweather.com/currentconditions/v1/331595?apikey=vnwz1buClrE9YhGJFG3mhNVq23tnIACH&details=true'
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    weather_status = api_data[0]['WeatherText']
    temp = api_data[0]['Temperature']['Metric']['Value']
    feels_like_temp = api_data[0]['RealFeelTemperature']['Metric']['Value']
    hum = api_data[0]['RelativeHumidity']
    dew_point = api_data[0]['DewPoint']['Metric']['Value']
    wind_direction = api_data[0]['Wind']['Direction']['Localized']
    wind_speed = api_data[0]['Wind']['Speed']['Metric']['Value']
    vs = api_data[0]['Visibility']['Metric']['Value']
    pr = api_data[0]['Pressure']['Metric']['Value']
    n = 1
    now = datetime.now() + timedelta(hours = n)
    time_name = now.strftime('%H:%M:%S')
    sun_time1 = '21:34:00'
    sun_time2 = '23:59:59'
    sun_time3 = '00:00:00'
    sun_time4 = '04:49:00'

    if time_name >= sun_time1 and time_name <= sun_time2 and weather_status == 'Clear':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-clear.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time1 and time_name <= sun_time2 and weather_status == 'Mostly clear':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-mostly-clear.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time1 and time_name <= sun_time2 and weather_status == 'Partly cloudy':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-partly-cloudy.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time1 and time_name <= sun_time2 and weather_status == 'Intermittent clouds':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-intermittent-clouds.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time1 and time_name <= sun_time2 and weather_status == 'Hazy moonlight':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('hazy-moonlight.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time1 and time_name <= sun_time2 and weather_status == 'Mostly cloudy':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-mostly-cloudy.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time3 and time_name <= sun_time4 and weather_status == 'Clear':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-clear.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time3 and time_name <= sun_time4 and weather_status == 'Mostly clear':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-mostly-clear.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time3 and time_name <= sun_time4 and weather_status == 'Partly cloudy':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-partly-cloudy.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time3 and time_name <= sun_time4 and weather_status == 'Intermittent clouds':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-intermittent-clouds.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time3 and time_name <= sun_time4 and weather_status == 'Hazy moonlight':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('hazy-moonlight.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if time_name >= sun_time3 and time_name <= sun_time4 and weather_status == 'Mostly cloudy':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-mostly-cloudy.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    if weather_status == 'Partly sunny':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('partly sunny.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    elif weather_status == 'Mostly sunny':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('mostly sunny.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    elif weather_status == 'Mostly cloudy':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('mostly cloudy.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    elif weather_status == 'Sunny':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('sunny.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    elif weather_status == 'Cloudy':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('cloudy.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    elif weather_status == 'Showers':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('showers.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    elif weather_status == 'Rain':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('rain.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    elif weather_status == 'Light rain':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('showers.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
    elif weather_status == 'Intermittent clouds':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('intermittent clouds.png'),
                         className = 'weather_image'),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
            html.P(weather_status + '. ' + 'Feels like ' + '{0:,.0f}°C'.format(feels_like_temp) + '.',
                   className = 'feels_like_temp_value'
                   ),
            html.Div([
                html.Div([
                    html.Div([
                        html.P('Wind speed: ' + '{0:,.0f}km/h'.format(wind_speed),
                               className = 'speed'
                               ),
                        html.P('Direction: ' + wind_direction,
                               className = 'direction'
                               ),
                    ], className = 's_d_p1'),
                    html.Div([
                        html.P('Humidity: ' + '{0:.0f}%'.format(hum),
                               className = 'humidity'
                               ),
                        html.P('Pressure: ' + '{0:.0f}mb'.format(pr),
                               className = 'pressure'
                               ),
                    ], className = 's_d_p2'),
                    html.Div([
                        html.P('Dew point: ' + '{0:.0f}°C'.format(dew_point),
                               className = 'dew_point'
                               ),
                        html.P('Visibility: ' + '{0:.1f}km'.format(vs),
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                    html.Div([
                        html.P('Sun Rise: ' + sun_rise_time,
                               className = 'dew_point'
                               ),
                        html.P('Sun Set: ' + sun_set_time,
                               className = 'visibility'
                               ),
                    ], className = 's_d_p3'),
                ], className = 'bg_color1')
            ], className = 'bg_color2')
        ]
