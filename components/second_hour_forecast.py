import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
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


def second_hour_forecast_weather_value(n_intervals):
    header_list = ['Time', 'Weather Status', 'Temperature', 'Real Feel Temperature', 'Precipitation']
    df = pd.read_csv('second_hour_forecast_data.csv', names = header_list)
    tme = df['Time'].tail(1).iloc[0]
    weather_status = df['Weather Status'].tail(1).iloc[0]
    temp = df['Temperature'].tail(1).iloc[0]
    real_feel_temp = df['Real Feel Temperature'].tail(1).iloc[0]
    pr = df['Precipitation'].tail(1).iloc[0]

    return [
        html.Div([
            html.Div([
                html.P('14:00', className = 'time'),
                html.Img(src = app.get_asset_url('partly sunny.png'),
                         className = 'weather_image'),
                html.P('RealFeel ' + '{0:,.0f}°C'.format(real_feel_temp),
                       className = 'real_feel_temp'
                       ),
                html.P('{0:,.0f}°C'.format(temp),
                       className = 'forecast_temperature_value'
                       ),
                html.Div([
                    html.Img(src = app.get_asset_url('pre.png'),
                             className = 'forecast_pre_image'),
                    html.P('{0:,.0f}%'.format(pr),
                           className = 'forecast_pre_value'
                           ),
                ], className = 'forecast_pre_row')
            ], className = 'forecast_bg')
        ], className = 'forecast_card'),
    ]
