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


def solar_today_power_chart_value(n_intervals):
    header_list = ['Date Time', 'Voltage', 'Current']
    df = pd.read_csv('sensors_data.csv', names = header_list)
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df['Date'] = df['Date Time'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    today_date = df['Date'].unique()
    date_time = df[df['Date'] == today_date[-1]]['Date Time'].tail(100)
    today_voltage = df[df['Date'] == today_date[-1]]['Voltage'].tail(100)
    today_current = df[df['Date'] == today_date[-1]]['Current'].tail(100)
    power_watt = today_voltage * today_current

    return {
        'data': [go.Scatter(
            x = date_time,
            y = power_watt,
            mode = 'lines',
            line = dict(width = 2, color = '#F1AB4D'),
            hoverinfo = 'text',
            hovertext =
            '<b>Time</b>: ' + date_time.astype(str) + '<br>' +
            '<b>Today Power</b>: ' + [f'{x:,.5f} W' for x in power_watt] + '<br>'
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
                'color': 'white',
                'size': 17},
            hovermode = 'closest',
            margin = dict(t = 50, r = 40),
            xaxis = dict(range = [min(date_time), max(date_time)],
                         title = '<b>Time</b>',
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

            yaxis = dict(range = [min(power_watt), max(power_watt)],
                         title = '<b>Today Power (Wh)</b>',
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
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'white')

        )

    }
