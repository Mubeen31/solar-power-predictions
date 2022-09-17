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
from google.oauth2 import service_account
import pandas_gbq as pd1
import pandas as pd2


font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

html.Div([
    dcc.Interval(id = 'update_date_time_value',
                 interval = 64000,
                 n_intervals = 0),
]),


def solar_current_power_chart_value(n_intervals):
    header_list = ['DateTime', 'Voltage', 'ValueCurrent']
    df1 = pd2.read_csv('Solar data 25-06-2022 to 12-09-2022.csv', names = header_list)
    credentials = service_account.Credentials.from_service_account_file('solardata-key.json')
    project_id = 'solardata-360222'
    df_sql = f"""SELECT
                    DateTime,
                    Voltage,
                    ValueCurrent
                    FROM `solardata-360222.SolarSensorsData.SensorsData`
                    ORDER BY DateTime
                    """
    df2 = pd1.read_gbq(df_sql, project_id = project_id, dialect = 'standard', credentials = credentials)
    df = pd2.concat([df1, df2], axis = 0, join = "inner", ignore_index = True)
    df['Power (W)'] = df['Voltage'] * df['ValueCurrent']
    df['Power (KW)'] = df['Power (W)'] / 1000
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    df['Date'] = df['DateTime'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['DateTime']).dt.time
    df['Hour'] = pd.to_datetime(df['DateTime']).dt.hour
    df['Time'] = df['Time'].astype(str)
    # df['Hour'] = df['Hour'].astype(str)
    rearrange_columns = ['DateTime', 'Date', 'Time', 'Hour', 'Voltage', 'ValueCurrent', 'Power (W)', 'Power (KW)']
    df = df[rearrange_columns]
    date_time = df['DateTime'].tail(60)
    get_voltage = df['Voltage'].tail(60)
    get_current = df['ValueCurrent'].tail(60)
    power_watt = get_voltage * get_current

    return {
        'data': [go.Bar(
            x = date_time,
            y = power_watt,
            marker = dict(color = '#00cc00'),
            hoverinfo = 'text',
            hovertext =
            '<b>Time</b>: ' + date_time.astype(str) + '<br>' +
            '<b>Current Power</b>: ' + [f'{x:,.5f} W' for x in power_watt] + '<br>'
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
                         title = '<b>Current Power (W)</b>',
                         color = '#1a1a1a',
                         zeroline = False,
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
                color = 'black')

        )

    }
