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


def forecast_weather_value(n_intervals):
    header_list = ['Date Time', 'Weather Status', 'Temperature', 'Real Feel Temperature', 'Humidity', 'Dew Point',
                   'Wind Direction', 'Wind Speed', 'Visibility', 'Pressure']
    df = pd.read_csv('accu_weather_data.csv', names = header_list)
    weather_status = df['Weather Status'].tail(1).iloc[0]
    temp = df['Temperature'].tail(1).iloc[0]
    feels_like_temp = df['Real Feel Temperature'].tail(1).iloc[0]
    wind_speed = df['Wind Speed'].tail(1).iloc[0]
    wind_direction = df['Wind Direction'].tail(1).iloc[0]
    hum = df['Humidity'].tail(1).iloc[0]
    pr = df['Pressure'].tail(1).iloc[0]
    dew_point = df['Dew Point'].tail(1).iloc[0]
    vs = df['Visibility'].tail(1).iloc[0]

    return [
        html.Div([
            html.Div([
                html.Div([
                    html.P('14:00', className = 'time'),
                    html.Img(src = app.get_asset_url('partly sunny.png'),
                             className = 'weather_image'),
                    html.P(weather_status,
                           className = 'forecast_weather_status'
                           ),
                    html.P('{0:,.0f}°C'.format(temp),
                           className = 'forecast_temperature_value'
                           ),
                    html.Div([
                        html.Img(src = app.get_asset_url('pre.png'),
                                 className = 'forecast_pre_image'),
                        html.P('52%',
                               className = 'forecast_pre_value'
                               ),
                    ], className = 'forecast_pre_row')
                ], className = 'forecast_bg')
            ], className = 'forecast_card'),
            html.Div([
                html.Div([
                    html.P('15:00', className = 'time'),
                    html.Img(src = app.get_asset_url('partly sunny.png'),
                             className = 'weather_image'),
                    html.P(weather_status,
                           className = 'forecast_weather_status'
                           ),
                    html.P('{0:,.0f}°C'.format(temp),
                           className = 'forecast_temperature_value'
                           ),
                    html.Div([
                        html.Img(src = app.get_asset_url('pre.png'),
                                 className = 'forecast_pre_image'),
                        html.P('52%',
                               className = 'forecast_pre_value'
                               ),
                    ], className = 'forecast_pre_row')
                ], className = 'forecast_bg')
            ], className = 'forecast_card'),
            html.Div([
                html.Div([
                    html.P('16:00', className = 'time'),
                    html.Img(src = app.get_asset_url('partly sunny.png'),
                             className = 'weather_image'),
                    html.P(weather_status,
                           className = 'forecast_weather_status'
                           ),
                    html.P('{0:,.0f}°C'.format(temp),
                           className = 'forecast_temperature_value'
                           ),
                    html.Div([
                        html.Img(src = app.get_asset_url('pre.png'),
                                 className = 'forecast_pre_image'),
                        html.P('52%',
                               className = 'forecast_pre_value'
                               ),
                    ], className = 'forecast_pre_row')
                ], className = 'forecast_bg')
            ], className = 'forecast_card')
        ], className = 'forecast_cards_row')
    ]
