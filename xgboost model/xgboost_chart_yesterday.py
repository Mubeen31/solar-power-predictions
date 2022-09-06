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
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import sqlalchemy
from dash import dash_table as dt
import time
from components.select_date import training_dataset_date

header_list = ['Date Time', 'Voltage', 'Current']
df = pd.read_csv('https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/sensors_data.csv',
                 names = header_list)
df['Power (W)'] = df['Voltage'] * df['Current']
df['Power (KW)'] = df['Power (W)'] / 1000
df['Date Time'] = pd.to_datetime(df['Date Time'])
df['Date'] = df['Date Time'].dt.date
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = pd.to_datetime(df['Date']).dt.month
df['time'] = pd.to_datetime(df['Date Time']).dt.time
df['hour'] = pd.to_datetime(df['Date Time']).dt.hour
df['time'].iloc[-1].strftime('%H:%M')
df['time'] = df['time'].astype(str)
df['hour'] = df['hour'].astype(str)
df['Time'] = pd.to_datetime(df['Date Time']).dt.time
df['Hour'] = pd.to_datetime(df['Date Time']).dt.hour
df['Time'] = df['Time'].astype(str)
today_date = df['Date'].unique()
rearrange_columns = ['Date Time', 'Date', 'Time', 'Hour', 'Voltage', 'Current', 'Power (W)', 'Power (KW)']
df = df[rearrange_columns]
unique_date = df['Date'].unique()
# filter_daily_values = df[(df['Date'] > '2022-08-11') & (df['Date'] <= unique_date[-2])][
#     ['Date', 'Hour', 'Power (KW)']]
# daily_hourly_values = filter_daily_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
#
# header_list = ['Date', 'Time', 'SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
#                'DewPoint (°C)',
#                'Wind (km/h)',
#                'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
#                'RainProbability (%)',
#                'CloudCover (%)']
# weather_data = pd.read_csv(
#     'https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/hourly_weather_forecasted_data.csv',
#     names = header_list,
#     encoding = 'unicode_escape')
# weather_data['UV Index Text'] = pd.factorize(weather_data['UVIndexText'])[0]
# weather_data.drop(['Date', 'Time', 'DewPoint (°C)', 'Direction', 'Visibility (km)',
#                    'UVIndexText', 'PreProbability (%)', 'RainProbability (%)', 'weather status', 'Hum (%)',
#                    'CloudCover (%)'], axis = 1, inplace = True)
#
# df1 = pd.concat([daily_hourly_values, weather_data], axis = 1)
# df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
# df1.loc[df1['SolarIrradiance (W/m2)'] == 0, ['Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']] = 0

filter_last_day_values = df[df['Date'] == unique_date[-2]][['Date', 'Hour', 'Power (KW)']]
last_day_hourly_values = filter_last_day_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
last_day_hourly_values_sum = last_day_hourly_values['Power (KW)'].sum()

filter_yes_values = df[(df['Date'] >= training_dataset_date) & (df['Date'] <= unique_date[-3])][
    ['Date', 'Hour', 'Power (KW)']]
yes_hourly_values = filter_yes_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
header_list = ['Date', 'Time', 'SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
               'DewPoint (°C)', 'Wind (km/h)',
               'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
               'RainProbability (%)',
               'CloudCover (%)']
weather_data1 = pd.read_csv(
    'https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/hourly_weather_forecasted_data.csv',
    names = header_list, encoding = 'unicode_escape')
weather_data1['UV Index Text'] = pd.factorize(weather_data1['UVIndexText'])[0]
weather_data1.loc[
    weather_data1['SolarIrradiance (W/m2)'] == 0, ['Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
                                                   'UV Index Text']] = 0
weather_unique_date = weather_data1['Date'].unique()
filter_weather_yes_values = \
    weather_data1[(weather_data1['Date'] >= training_dataset_date) & (weather_data1['Date'] <= weather_unique_date[-3])][
        ['Date', 'SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
         'UV Index Text']].reset_index()
filter_weather_yes_values.drop(['index'], axis = 1, inplace = True)

yes_df1 = pd.concat([yes_hourly_values, filter_weather_yes_values], axis = 1)
yes_df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
yes_count_total_rows = len(yes_df1)
yes_independent_columns = yes_df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
                                   'UV Index Text']][
                          0:yes_count_total_rows]
yes_independent_columns1 = yes_df1[
                               ['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
                                'UV Index Text']][
                           0:yes_count_total_rows]
yes_dependent_column = yes_df1['Power (KW)'][0:yes_count_total_rows]
yes_reg = XGBRegressor()
yes_reg.fit(yes_independent_columns, yes_dependent_column)
forcasted_yes_values = weather_data1[(weather_data1['Date'] == weather_unique_date[-2])][
    ['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']]
forcasted_yes_values1 = weather_data1[(weather_data1['Date'] == weather_unique_date[-2])][
    ['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']]
return_array = yes_reg.predict(forcasted_yes_values)
predicted_data = pd.DataFrame(return_array, columns = ['Power (KW)'])
predicted_data.to_csv('yesterday_predicted_chart_data.csv', index = False)
