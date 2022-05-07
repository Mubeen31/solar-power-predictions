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


def current_weather_value(n_intervals):
    header_list = ['Date Time', 'Weather Status', 'Temperature', 'Real Feel Temperature', 'Humidity', 'Dew Point',
                   'Wind Direction', 'Wind Speed', 'Visibility', 'Pressure']
    df = pd.read_csv('accu_weather_data.csv', names = header_list)
    weather_status = df['Weather Status'].tail(1).iloc[0]
    temp = df['Temperature'].tail(1).iloc[0]
    feels_like_temp = df['Real Feel Temperature'].tail(1).iloc[0]

    if weather_status == 'Mostly sunny':
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
        ]
