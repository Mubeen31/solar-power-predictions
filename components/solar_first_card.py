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
    dcc.Interval(id = 'solar_wind_card',
                 interval = 30000,
                 n_intervals = 0),
]),


def solar_first_card_value(n_intervals):
    header_list = ['Date Time', 'Voltage', 'Current']
    df = pd.read_csv('sensors_data.csv', names = header_list)
    get_voltage = df['Voltage'].tail(1).iloc[0]
    get_current = df['Current'].tail(1).iloc[0]
    power_watt = get_voltage * get_current
    power_kilo_watt = power_watt / 1000

    return [
        html.P('Current Solar Power', className = 'card_text'),
        html.Div([
            html.P('{0:,.5f}'.format(abs(power_kilo_watt)) + ' ' + 'KW',
                   className = 'card_value1'),
            html.P('{0:,.5f}'.format(abs(power_watt)) + ' ' + 'W',
                   className = 'card_value2')
        ], className = 'card_values_gap'),
        html.Div([
            html.P('Voltage: ' + '{0:,.2f}'.format(get_voltage) + ' ' + 'V',
                   className = 'card_value3'),
            html.P('Current: ' + '{0:,.2f}'.format(abs(get_current)) + ' ' + 'A',
                   className = 'card_value4')
        ], className = 'card_value_3_4')
    ]
