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
                 interval = 1000,
                 n_intervals = 0),
]),


def solar_current_power_chart_value(n_intervals):
    header_list = ['Date Time', 'Voltage', 'Current']
    df = pd.read_csv('sensors_data.csv', names = header_list)
    date_time = df['Date Time'].tail(30)
    get_voltage = df['Voltage'].tail(30)
    get_current = df['Current'].tail(30)
    power_watt = get_voltage * get_current
    power_kilo_watt = power_watt / 1000

    return {
        'data': [go.Bar(
            x = date_time,
            y = power_watt,
            # fill = 'tonexty',
            # fillcolor = 'rgba(255, 0, 255, 0.1)',
            # mode = 'lines',
            # line = dict(width = 2, color = '#ff00ff'),
            # marker = dict(size = 7, symbol = 'circle', color = '#D35400',
            #               line = dict(color = '#D35400', width = 2)
            #               ),

            hoverinfo = 'text',
            hovertext =
            '<b>Time</b>: ' + date_time.astype(str) + '<br>' +
            '<b></b>: ' + [f'{x:,.5f} W' for x in power_watt] + '<br>'

        )],

        'layout': go.Layout(
            # paper_bgcolor = 'rgba(0,0,0,0)',
            # plot_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'black',
            paper_bgcolor = 'black',
            title = {
                'text': '',

                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': 'white',
                'size': 17},

            hovermode = 'x unified',
            margin = dict(t = 25, r = 10, l = 70),

            xaxis = dict(range = [min(date_time), max(date_time)],
                         title = '<b>Time</b>',
                         color = 'white',
                         showspikes = True,
                         showline = True,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            yaxis = dict(range = [min(power_watt), max(power_watt)],
                         title = '<b></b>',
                         color = 'white',
                         showspikes = False,
                         showline = True,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            # legend = {
            #     'orientation': 'h',
            #     'bgcolor': '#F2F2F2',
            #     'x': 0.5,
            #     'y': 1.25,
            #     'xanchor': 'center',
            #     'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'white')

        )

    }
