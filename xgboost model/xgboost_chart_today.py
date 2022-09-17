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
from xgboost import XGBRegressor
import sqlalchemy
from dash import dash_table as dt
import time
import csv
from components.select_date import training_dataset_date
from google.oauth2 import service_account
import pandas_gbq as pd1
import pandas as pd2

now = datetime.now()
time_name = now.strftime('%H:%M:%S')
header_list = ['DateTime', 'Voltage', 'ValueCurrent']
df1 = pd2.read_csv('Solar data 25-06-2022 to 12-09-2022.csv', names = header_list)
credentials = service_account.Credentials.from_service_account_file('solardata-key.json')
project_id = 'solardata-360222'
df_sql = f"""SELECT
                DateTime,
                Voltage,
                ValueCurrent
                FROM `solardata-360222.SolarSensorsData.SensorsData`
                ORDER BY DateTime
                """
df2 = pd1.read_gbq(df_sql, project_id = project_id, dialect = 'standard', credentials = credentials)
df = pd2.concat([df1, df2], axis = 0, join = "inner", ignore_index = True)
df['Power (W)'] = df['Voltage'] * df['ValueCurrent']
df['Power (KW)'] = df['Power (W)'] / 1000
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date'] = df['DateTime'].dt.date
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['DateTime']).dt.time
df['Hour'] = pd.to_datetime(df['DateTime']).dt.hour
df['Time'] = df['Time'].astype(str)
# df['Hour'] = df['Hour'].astype(str)
rearrange_columns = ['DateTime', 'Date', 'Time', 'Hour', 'Voltage', 'ValueCurrent', 'Power (W)', 'Power (KW)']
df = df[rearrange_columns]
unique_date = df['Date'].unique()
filter_daily_values = df[(df['Date'] >= training_dataset_date) & (df['Date'] <= unique_date[-2])][
    ['Date', 'Hour', 'Power (KW)']]
daily_hourly_values = filter_daily_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()

header_list = ['Date', 'Time', 'SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
               'DewPoint (°C)',
               'Wind (km/h)',
               'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
               'RainProbability (%)',
               'CloudCover (%)']
weather_data = pd.read_csv(
    'https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/hourly_weather_forecasted_data.csv',
    names = header_list,
    encoding = 'unicode_escape')
weather_data['UV Index Text'] = pd.factorize(weather_data['UVIndexText'])[0]
weather_data.loc[
    weather_data['SolarIrradiance (W/m2)'] == 0, ['weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
                                                  'DewPoint (°C)', 'Wind (km/h)',
                                                  'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex',
                                                  'UVIndexText', 'PreProbability (%)', 'RainProbability (%)',
                                                  'CloudCover (%)', 'UV Index Text']] = 0
unique_weather_date = weather_data['Date'].unique()
hourly_weather = \
    weather_data[(weather_data['Date'] >= training_dataset_date) & (weather_data['Date'] <= unique_weather_date[-2])][
        ['Date', 'Time', 'SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
         'DewPoint (°C)', 'Wind (km/h)',
         'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
         'RainProbability (%)',
         'CloudCover (%)', 'UV Index Text']].reset_index()
hourly_weather.drop(['index', 'Date', 'Time', 'Direction', 'Visibility (km)',
                     'UVIndexText', 'PreProbability (%)', 'RainProbability (%)', 'weather status',
                     'CloudCover (%)', 'Hum (%)', 'DewPoint (°C)'], axis = 1, inplace = True)

df1 = pd.concat([daily_hourly_values, hourly_weather], axis = 1)
df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
df1.loc[df1['SolarIrradiance (W/m2)'] == 0, ['Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
                                             'UV Index Text']] = 0

if time_name >= '00:00:00' and time_name <= '11:59:59':
    count_total_rows = len(df1)
    independent_columns = df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
                               'UV Index Text']][
                          0:count_total_rows]
    dependent_column = df1['Power (KW)'][0:count_total_rows]

    reg = XGBRegressor()
    reg.fit(independent_columns, dependent_column)

    forcasted_data = weather_data[
        ['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']].tail(
        12)

    return_array = list(reg.predict(forcasted_data))

    date = now.strftime('%Y-%m-%d')
    current_date_12 = [date, date, date, date, date, date, date, date, date, date, date, date]

    hours_12 = list(daily_hourly_values['Hour'][0:12])

    data_dict = {'Date': current_date_12, 'Hour': hours_12, 'Power (KW)': return_array}

    data_dataframe = pd.DataFrame(data_dict)
    data_dataframe.to_csv('today_predicted_chart_data.csv', index = False)

elif time_name >= '12:00:00' and time_name <= '23:59:59':
    count_total_rows = len(df1)
    independent_columns = df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
                               'UV Index Text']][
                          0:count_total_rows]
    dependent_column = df1['Power (KW)'][0:count_total_rows]

    reg = XGBRegressor()
    reg.fit(independent_columns, dependent_column)

    forcasted_data = weather_data[
        ['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']].tail(
        24)

    return_array = list(reg.predict(forcasted_data))

    date = now.strftime('%Y-%m-%d')
    current_date_24 = [date, date, date, date, date, date, date, date, date, date, date, date, date, date, date,
                       date, date, date, date, date, date, date, date, date]

    hours_24 = list(daily_hourly_values['Hour'][0:24])

    data_dict = {'Date': current_date_24, 'Hour': hours_24, 'Power (KW)': return_array}

    data_dataframe = pd.DataFrame(data_dict)
    data_dataframe.to_csv('today_predicted_chart_data.csv', index = False)
