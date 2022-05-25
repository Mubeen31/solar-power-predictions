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


def first_hour_forecast_weather_value(n_intervals):
    header_list = ['Time', 'Weather Status', 'Temperature', 'Real Feel Temperature', 'Precipitation']
    df = pd.read_csv('first_hour_forecast_data.csv', names = header_list)
    df['Time'] = pd.to_datetime(df['Time'])
    df['time'] = pd.to_datetime(df['Time']).dt.time
    tme = df['time'].iloc[-1].strftime('%H:%M')
    weather_status = df['Weather Status'].tail(1).iloc[0]
    temp = df['Temperature'].tail(1).iloc[0]
    real_feel_temp = df['Real Feel Temperature'].tail(1).iloc[0]
    pr = df['Precipitation'].tail(1).iloc[0]

    if weather_status == 'Partly sunny':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
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
    elif weather_status == 'Mostly sunny':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
                    html.Img(src = app.get_asset_url('mostly sunny.png'),
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
    elif weather_status == 'Mostly cloudy':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
                    html.Img(src = app.get_asset_url('mostly cloudy.png'),
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
    elif weather_status == 'Sunny':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
                    html.Img(src = app.get_asset_url('sunny.png'),
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
    elif weather_status == 'Cloudy':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
                    html.Img(src = app.get_asset_url('cloudy.png'),
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
    elif weather_status == 'Showers':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
                    html.Img(src = app.get_asset_url('showers.png'),
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
    elif weather_status == 'Rain':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
                    html.Img(src = app.get_asset_url('rain.png'),
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
    elif weather_status == 'Light rain':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
                    html.Img(src = app.get_asset_url('showers.png'),
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
    elif weather_status == 'Intermittent clouds':
        return [
            html.Div([
                html.Div([
                    html.P(tme, className = 'time'),
                    html.Img(src = app.get_asset_url('intermittent clouds.png'),
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
