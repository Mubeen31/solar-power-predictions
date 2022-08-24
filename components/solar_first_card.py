import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
from datetime import datetime, date, time
from sklearn import linear_model
import sqlalchemy
from dash import dash_table as dt
import time
from google.oauth2 import service_account  # pip install google-auth
import pandas_gbq  # pip install pandas-gbq

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

html.Div([
    dcc.Interval(id = 'update_date_time_value',
                 interval = 60000,
                 n_intervals = 0),
]),


def solar_first_card_value(n_intervals):
    # header_list = ['Date Time', 'Voltage', 'Current']
    # df = pd.read_csv('https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/sensors_data.csv', names = header_list)
    credentials = service_account.Credentials.from_service_account_file('D:\solar energy monitoring and prediction system\solar power\components\solardata-key.json')
    project_id = 'solardata-360222'  # make sure to change this with your own project ID
    df_voltage = f"""
    SELECT *
  FROM `SolarPowerGeneration.sensors-data`
 ORDER
    BY Voltage DESC
 LIMIT 1
    """
    df = pd.read_gbq(df_voltage, project_id = project_id, dialect = 'standard', credentials = credentials)
    get_voltage = df['Voltage'].tail(1).iloc[0]
    # get_current = df['Current'].tail(1).iloc[0]
    # power_watt = get_voltage * get_current
    # power_kilo_watt = power_watt / 1000

    return [
        html.P('Current Solar Power', className = 'card_text'),
        html.Div([
            html.P('{0:,.5f}'.format(abs(get_voltage)) + ' ' + 'KW',
                   className = 'card_value1'),
            html.P('{0:,.5f}'.format(abs(get_voltage)) + ' ' + 'W',
                   className = 'card_value2')
        ], className = 'card_values_gap'),
        html.Div([
            html.P('Voltage: ' + '{0:,.2f}'.format(get_voltage) + ' ' + 'V',
                   className = 'card_value3'),
            html.P('Current: ' + '{0:,.2f}'.format(abs(get_voltage)) + ' ' + 'A',
                   className = 'card_value4')
        ], className = 'card_value_3_4')
    ]
