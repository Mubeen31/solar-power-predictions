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


def energy_forecasting_chart_value(n_intervals):
    # now = datetime.now()
    # time_name = now.strftime('%H:%M:%S')
    # if time_name >= '23:30:00' and time_name <= '00:00:00' and time_name >= '00:00:00' and time_name <= '11:30:00':
    #     raise PreventUpdate
    # else:
    header_list = ['Date Time', 'Voltage', 'Current']
    df = pd.read_csv('sensors_data.csv', names = header_list)
    df['Power (W)'] = df['Voltage'] * df['Current']
    df['Power (KW)'] = df['Power (W)'] / 1000
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df['Date'] = df['Date Time'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Date Time']).dt.time
    df['Hour'] = pd.to_datetime(df['Date Time']).dt.hour
    df['Time'] = df['Time'].astype(str)
    # df['Hour'] = df['Hour'].astype(str)
    rearrange_columns = ['Date Time', 'Date', 'Time', 'Hour', 'Voltage', 'Current', 'Power (W)', 'Power (KW)']
    df = df[rearrange_columns]
    unique_date = df['Date'].unique()
    filter_daily_values = df[(df['Date'] >= unique_date[-3]) & (df['Date'] <= unique_date[-2])][
        ['Date', 'Hour', 'Power (KW)']]
    daily_hourly_values = filter_daily_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()

    header_list = ['SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)', 'DewPoint (°C)',
                   'Wind (km/h)',
                   'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
                   'RainProbability (%)',
                   'CloudCover (%)']
    weather_data = pd.read_csv('hourly_weather_forecasted_data.csv', names = header_list,
                               encoding = 'unicode_escape')
    weather_data.drop(
        ['RealFeelTemp (°C)', 'DewPoint (°C)', 'Wind (km/h)', 'Direction', 'Visibility (km)', 'UVIndex',
         'UVIndexText', 'PreProbability (%)', 'RainProbability (%)', 'weather status'], axis = 1,
        inplace = True)

    df1 = pd.concat([daily_hourly_values, weather_data], axis = 1)
    df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
    df1.loc[df1['SolarIrradiance (W/m2)'] == 0, ['Temp (°C)', 'Hum (%)', 'CloudCover (%)']] = 0

    count_total_rows = len(df1) - 24
    independent_columns = df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'Hum (%)', 'CloudCover (%)']][
                          0:count_total_rows]
    dependent_column = df1['Power (KW)'][0:count_total_rows]

    reg = linear_model.LinearRegression()
    reg.fit(independent_columns, dependent_column)

    forcasted_data = df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'Hum (%)', 'CloudCover (%)']].tail(24)

    return_array = list(reg.predict(forcasted_data))

    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    current_date = [date, date, date, date, date, date, date, date, date, date, date, date, date, date, date, date,
                    date, date, date, date, date, date, date, date]

    hours = list(daily_hourly_values['Hour'][0:24])

    data_dict = {'Date': current_date, 'Hour': hours, 'Power (KW)': return_array}

    data_dataframe = pd.DataFrame(data_dict)

    # today data
    filter_today_values = df[df['Date'] == unique_date[-1]][['Date', 'Hour', 'Power (KW)']]
    today_hourly_values = filter_today_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()

    return {
        'data': [go.Scatter(
            x = today_hourly_values['Hour'],
            y = today_hourly_values['Power (KW)'],
            name = 'Today Solar Energy',
            mode = 'lines',
            line = dict(width = 2, color = '#F1AB4D'),
            hoverinfo = 'text',
            hovertext =
            '<b>Date</b>: ' + today_hourly_values['Date'].astype(str) + '<br>' +
            '<b>Hour</b>: ' + today_hourly_values['Hour'].astype(str) + '<br>' +
            '<b>Today Solar Energy</b>: ' + [f'{x:,.5f} KWh' for x in today_hourly_values['Power (KW)']] + '<br>'
        ),
            go.Scatter(
                x = data_dataframe['Hour'],
                y = data_dataframe['Power (KW)'],
                name = 'Today Predicted Solar Energy',
                mode = 'lines',
                line = dict(color = 'firebrick', dash = 'dash'),
                hoverinfo = 'text',
                hovertext =
                '<b>Date</b>: ' + data_dataframe['Date'].astype(str) + '<br>' +
                '<b>Hour</b>: ' + data_dataframe['Hour'].astype(str) + '<br>' +
                '<b>Predicted Solar Energy</b>: ' + [f'{x:,.5f} KWh' for x in data_dataframe['Power (KW)']] + '<br>'
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
            xaxis = dict(
                title = '<b>Hours</b>',
                color = '#1a1a1a',
                showline = True,
                tick0 = 0,
                dtick = 1,
                showgrid = False,
                linecolor = '#1a1a1a',
                linewidth = 1,
                ticks = 'outside',
                tickfont = dict(
                    family = 'Arial',
                    size = 12,
                    color = '#1a1a1a')

            ),

            yaxis = dict(
                title = '<b>Solar Energy (KWh)</b>',
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
            legend = {
                'orientation': 'h',
                'bgcolor': 'rgba(255, 255, 255, 0)',
                'x': 0.5,
                'y': 1.2,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black')

        )

    }