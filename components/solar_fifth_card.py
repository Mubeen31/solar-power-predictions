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


def solar_fifth_card_value(n_intervals):
    header_list = ['Date Time', 'Voltage', 'Current']
    df = pd.read_csv('sensors_data.csv', names = header_list)
    df['Power (W)'] = df['Voltage'] * df['Current']
    df['Power (KW)'] = df['Power (W)'] / 1000
    energy_watts = (df['Power (W)'].sum())
    energy_kilo_watts = (df['Power (KW)'].sum())

    return [
        html.P('Lifetime Solar Energy', className = 'card_text'),
        html.Div([
            html.P('{0:,.2f}'.format(energy_kilo_watts) + ' ' + 'KWh',
                   className = 'card_value1'),
            html.P('{0:,.2f}'.format(energy_watts) + ' ' + 'Wh',
                   className = 'card_value2')
        ], className = 'card_values_gap')
    ]