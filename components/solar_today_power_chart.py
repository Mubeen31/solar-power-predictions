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
from google.oauth2 import service_account
import pandas_gbq as pd1
import pandas as pd2

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

html.Div([
    dcc.Interval(id = 'update_date_time_value',
                 interval = 64000,
                 n_intervals = 0),
]),


def solar_today_power_chart_value(n_intervals):
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
    df['time'] = pd.to_datetime(df['DateTime']).dt.time
    df['hour'] = pd.to_datetime(df['DateTime']).dt.hour
    df['time'].iloc[-1].strftime('%H:%M')
    df['time'] = df['time'].astype(str)
    df['hour'] = df['hour'].astype(str)
    today_date = df['Date'].unique()
    n = 1
    now = datetime.now() + timedelta(hours=n)
    time_name = now.strftime('%H:%M:%S')

    if time_name >= '00:00:00' and time_name <= '00:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy]
        hours = [0]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '01:00:00' and time_name <= '01:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy]
        hours = [0, 1]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '02:00:00' and time_name <= '02:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy]
        hours = [0, 1, 2]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '03:00:00' and time_name <= '03:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy]
        hours = [0, 1, 2, 3]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '04:00:00' and time_name <= '04:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy]
        hours = [0, 1, 2, 3, 4]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '05:00:00' and time_name <= '05:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '06:00:00' and time_name <= '06:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '07:00:00' and time_name <= '07:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '08:00:00' and time_name <= '08:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '09:00:00' and time_name <= '09:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '10:00:00' and time_name <= '10:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '11:00:00' and time_name <= '11:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '12:00:00' and time_name <= '12:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '13:00:00' and time_name <= '13:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '14:00:00' and time_name <= '14:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '15:00:00' and time_name <= '15:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '16:00:00' and time_name <= '16:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

        seventeenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
        seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '17:00:00' and time_name <= '17:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

        seventeenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
        seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()

        eighteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '17:00:00') & (df['time'] <= '17:59:59')]
        eighteenth_hour_energy = eighteenth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy, eighteenth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '18:00:00' and time_name <= '18:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

        seventeenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
        seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()

        eighteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '17:00:00') & (df['time'] <= '17:59:59')]
        eighteenth_hour_energy = eighteenth_hour['Power (KW)'].sum()

        nineteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '18:00:00') & (df['time'] <= '18:59:59')]
        nineteenth_hour_energy = nineteenth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy, eighteenth_hour_energy,
                       nineteenth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '19:00:00' and time_name <= '19:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

        seventeenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
        seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()

        eighteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '17:00:00') & (df['time'] <= '17:59:59')]
        eighteenth_hour_energy = eighteenth_hour['Power (KW)'].sum()

        nineteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '18:00:00') & (df['time'] <= '18:59:59')]
        nineteenth_hour_energy = nineteenth_hour['Power (KW)'].sum()

        twenteeth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '19:00:00') & (df['time'] <= '19:59:59')]
        twenteeth_hour_energy = twenteeth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy, eighteenth_hour_energy,
                       nineteenth_hour_energy, twenteeth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '20:00:00' and time_name <= '20:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

        seventeenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
        seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()

        eighteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '17:00:00') & (df['time'] <= '17:59:59')]
        eighteenth_hour_energy = eighteenth_hour['Power (KW)'].sum()

        nineteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '18:00:00') & (df['time'] <= '18:59:59')]
        nineteenth_hour_energy = nineteenth_hour['Power (KW)'].sum()

        twenteeth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '19:00:00') & (df['time'] <= '19:59:59')]
        twenteeth_hour_energy = twenteeth_hour['Power (KW)'].sum()

        twentyoneth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '20:00:00') & (df['time'] <= '20:59:59')]
        twentyoneth_hour_energy = twentyoneth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy, eighteenth_hour_energy,
                       nineteenth_hour_energy, twenteeth_hour_energy, twentyoneth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '21:00:00' and time_name <= '21:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

        seventeenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
        seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()

        eighteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '17:00:00') & (df['time'] <= '17:59:59')]
        eighteenth_hour_energy = eighteenth_hour['Power (KW)'].sum()

        nineteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '18:00:00') & (df['time'] <= '18:59:59')]
        nineteenth_hour_energy = nineteenth_hour['Power (KW)'].sum()

        twenteeth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '19:00:00') & (df['time'] <= '19:59:59')]
        twenteeth_hour_energy = twenteeth_hour['Power (KW)'].sum()

        twentyoneth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '20:00:00') & (df['time'] <= '20:59:59')]
        twentyoneth_hour_energy = twentyoneth_hour['Power (KW)'].sum()

        twentysecond_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '21:00:00') & (df['time'] <= '21:59:59')]
        twentysecond_hour_energy = twentysecond_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy, eighteenth_hour_energy,
                       nineteenth_hour_energy, twenteeth_hour_energy, twentyoneth_hour_energy, twentysecond_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '22:00:00' and time_name <= '22:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

        seventeenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
        seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()

        eighteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '17:00:00') & (df['time'] <= '17:59:59')]
        eighteenth_hour_energy = eighteenth_hour['Power (KW)'].sum()

        nineteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '18:00:00') & (df['time'] <= '18:59:59')]
        nineteenth_hour_energy = nineteenth_hour['Power (KW)'].sum()

        twenteeth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '19:00:00') & (df['time'] <= '19:59:59')]
        twenteeth_hour_energy = twenteeth_hour['Power (KW)'].sum()

        twentyoneth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '20:00:00') & (df['time'] <= '20:59:59')]
        twentyoneth_hour_energy = twentyoneth_hour['Power (KW)'].sum()

        twentysecond_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '21:00:00') & (df['time'] <= '21:59:59')]
        twentysecond_hour_energy = twentysecond_hour['Power (KW)'].sum()

        twentythird_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '22:00:00') & (df['time'] <= '22:59:59')]
        twentythird_hour_energy = twentythird_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy, eighteenth_hour_energy,
                       nineteenth_hour_energy, twenteeth_hour_energy, twentyoneth_hour_energy, twentysecond_hour_energy,
                       twentythird_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)
    elif time_name >= '23:00:00' and time_name <= '23:59:59':
        first_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
        first_hour_energy = first_hour['Power (KW)'].sum()

        second_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
        second_hour_energy = second_hour['Power (KW)'].sum()

        third_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
        third_hour_energy = third_hour['Power (KW)'].sum()

        fourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
        fourth_hour_energy = fourth_hour['Power (KW)'].sum()

        fifth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
        fifth_hour_energy = fifth_hour['Power (KW)'].sum()

        sixth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
        sixth_hour_energy = sixth_hour['Power (KW)'].sum()

        seventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
        seventh_hour_energy = seventh_hour['Power (KW)'].sum()

        eighth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
        eighth_hour_energy = eighth_hour['Power (KW)'].sum()

        nineth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
        nineth_hour_energy = nineth_hour['Power (KW)'].sum()

        tenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
        tenth_hour_energy = tenth_hour['Power (KW)'].sum()

        eleventh_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
        eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

        twelth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
        twelth_hour_energy = twelth_hour['Power (KW)'].sum()

        thirteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
        thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

        fourteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
        fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

        fifteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
        fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

        sixteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
        sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

        seventeenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
        seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()

        eighteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '17:00:00') & (df['time'] <= '17:59:59')]
        eighteenth_hour_energy = eighteenth_hour['Power (KW)'].sum()

        nineteenth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '18:00:00') & (df['time'] <= '18:59:59')]
        nineteenth_hour_energy = nineteenth_hour['Power (KW)'].sum()

        twenteeth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '19:00:00') & (df['time'] <= '19:59:59')]
        twenteeth_hour_energy = twenteeth_hour['Power (KW)'].sum()

        twentyoneth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '20:00:00') & (df['time'] <= '20:59:59')]
        twentyoneth_hour_energy = twentyoneth_hour['Power (KW)'].sum()

        twentysecond_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '21:00:00') & (df['time'] <= '21:59:59')]
        twentysecond_hour_energy = twentysecond_hour['Power (KW)'].sum()

        twentythird_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '22:00:00') & (df['time'] <= '22:59:59')]
        twentythird_hour_energy = twentythird_hour['Power (KW)'].sum()

        twentyfourth_hour = df[(df['Date'] == today_date[-1]) & (df['time'] >= '23:00:00') & (df['time'] <= '23:59:59')]
        twentyfourth_hour_energy = twentyfourth_hour['Power (KW)'].sum()
        hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                       sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy,
                       tenth_hour_energy,
                       eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                       fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy, eighteenth_hour_energy,
                       nineteenth_hour_energy, twenteeth_hour_energy, twentyoneth_hour_energy, twentysecond_hour_energy,
                       twentythird_hour_energy, twentyfourth_hour_energy]
        hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
        hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)

    return {
        'data': [go.Scatter(
            x = hourly_data_and_hours_df['Hours'],
            y = hourly_data_and_hours_df['Hourly Data'],
            mode = 'lines',
            line = dict(width = 2, color = '#F1AB4D'),
            hoverinfo = 'text',
            hovertext =
            '<b>Hour</b>: ' + hourly_data_and_hours_df['Hours'].astype(str) + '<br>' +
            '<b>Solar Energy</b>: ' + [f'{x:,.5f} KWh' for x in hourly_data_and_hours_df['Hourly Data']] + '<br>'
        )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(255, 255, 255, 0)',
            paper_bgcolor = 'rgba(255, 255, 255, 0)',
            title = {
                'text': '',
                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': '#0000FF',
                'size': 17},
            hovermode = 'x unified',
            margin = dict(t = 50, r = 40),
            xaxis = dict(
                tick0 = 0,
                dtick = 1,
                title = '<b>Hours</b>',
                color = '#1a1a1a',
                showline = True,
                showgrid = False,
                linecolor = '#1a1a1a',
                linewidth = 1,
                ticks = 'outside',
                tickfont = dict(
                    family = 'Arial',
                    size = 12,
                    color = '#1a1a1a')

            ),

            yaxis = dict(
                title = '<b>Solar Energy (KWh)</b>',
                color = '#1a1a1a',
                zeroline = False,
                showline = True,
                showgrid = False,
                linecolor = '#1a1a1a',
                linewidth = 1,
                ticks = 'outside',
                tickfont = dict(
                    family = 'Arial',
                    size = 12,
                    color = '#1a1a1a')

            ),
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black')

        )

    }
