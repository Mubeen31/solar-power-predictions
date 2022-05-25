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

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

html.Div([
    dcc.Interval(id = 'update_date_time_value',
                 interval = 60000,
                 n_intervals = 0),
]),


def solar_third_card_value(n_intervals):
    header_list = ['Date Time', 'Voltage', 'Current']
    df = pd.read_csv('sensors_data.csv', names = header_list)
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df['Date'] = df['Date Time'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    today_date = df['Date'].unique()
    today_voltage = df[df['Date'] == today_date[-2]]['Voltage'].mean()
    today_current = df[df['Date'] == today_date[-2]]['Current'].mean()
    power_watt = today_voltage * today_current
    power_kilo_watt = power_watt / 1000

    return [
        html.P('Yesterday Solar Energy', className = 'card_text'),
        html.Div([
            html.P('{0:,.5f}'.format(abs(power_kilo_watt)) + ' ' + 'KW',
                   className = 'card_value1'),
            html.P('{0:,.5f}'.format(abs(power_watt)) + ' ' + 'W',
                   className = 'card_value2')
        ], className = 'card_values_gap')
    ]
