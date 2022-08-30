import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
from datetime import datetime, date, time
from datetime import timedelta
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
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

n_estimator_list = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]
random_state_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

dcc.Dropdown(id = 'select_trees',
             multi = False,
             clearable = True,
             disabled = False,
             style = {'display': True},
             value = 100,
             placeholder = 'Select trees',
             options = n_estimator_list,
             className = 'drop_down_list'),

dcc.Dropdown(id = 'select_random_state',
             multi = False,
             clearable = True,
             disabled = False,
             style = {'display': True},
             value = 0,
             placeholder = 'Select random states',
             options = random_state_list,
             className = 'drop_down_list'),


def random_forest_regression_chart_value(n_intervals, select_trees, select_random_state):
    if select_trees is None:
        raise PreventUpdate
    if select_random_state is None:
        raise PreventUpdate
    else:
        n = 1
        now = datetime.now() + timedelta(hours = n)
        time_name = now.strftime('%H:%M:%S')
        header_list = ['Date Time', 'Voltage', 'Current']
        df = pd.read_csv('https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/sensors_data.csv', names = header_list)
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
        filter_daily_values = df[(df['Date'] > '2022-06-24') & (df['Date'] <= unique_date[-2])][
            ['Date', 'Hour', 'Power (KW)']]
        daily_hourly_values = filter_daily_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()

        header_list = ['Date', 'Time', 'SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
                       'DewPoint (°C)',
                       'Wind (km/h)',
                       'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
                       'RainProbability (%)',
                       'CloudCover (%)']
        weather_data = pd.read_csv('https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/hourly_weather_forecasted_data.csv', names = header_list,
                                   encoding = 'unicode_escape')
        weather_data['UV Index Text'] = pd.factorize(weather_data['UVIndexText'])[0]
        weather_data.drop(['Date', 'Time', 'Direction', 'Visibility (km)',
                           'UVIndexText', 'PreProbability (%)', 'RainProbability (%)', 'weather status',
                           'CloudCover (%)', 'Hum (%)', 'DewPoint (°C)'], axis = 1,
                          inplace = True)

        df1 = pd.concat([daily_hourly_values, weather_data], axis = 1)
        df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
        df1.loc[df1['SolarIrradiance (W/m2)'] == 0, ['Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']] = 0

    if time_name >= '00:00:00' and time_name <= '11:59:59':
        count_total_rows = len(df1) - 12
        independent_columns = df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']][
                              0:count_total_rows]
        dependent_column = df1['Power (KW)'][0:count_total_rows]

        rfr = RandomForestRegressor(n_estimators = select_trees, random_state = select_random_state)
        rfr.fit(independent_columns, dependent_column)

        forcasted_data = df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']].tail(12)

        return_array = list(rfr.predict(forcasted_data))

        date = now.strftime('%Y-%m-%d')
        current_date_12 = [date, date, date, date, date, date, date, date, date, date, date, date]

        hours_12 = list(daily_hourly_values['Hour'][0:12])

        data_dict = {'Date': current_date_12, 'Hour': hours_12, 'Power (KW)': return_array}

        data_dataframe = pd.DataFrame(data_dict)

    elif time_name >= '12:00:00' and time_name <= '23:59:59':
        count_total_rows = len(df1) - 24
        independent_columns = df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']][
                              0:count_total_rows]
        dependent_column = df1['Power (KW)'][0:count_total_rows]

        rfr = RandomForestRegressor(n_estimators = select_trees, random_state = select_random_state)
        rfr.fit(independent_columns, dependent_column)

        forcasted_data = df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']].tail(24)

        return_array = list(rfr.predict(forcasted_data))

        date = now.strftime('%Y-%m-%d')
        current_date_24 = [date, date, date, date, date, date, date, date, date, date, date, date, date, date, date,
                           date, date, date, date, date, date, date, date, date]

        hours_24 = list(daily_hourly_values['Hour'][0:24])

        data_dict = {'Date': current_date_24, 'Hour': hours_24, 'Power (KW)': return_array}

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
                line = dict(color = 'firebrick', dash = 'dot'),
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
                'text': 'Random Forest Regression Model',
                'y': 0.88,
                'x': 0.28,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': '#0000FF',
                'size': 15},
            hovermode = 'x unified',
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
                'orientation': 'v',
                'bgcolor': 'rgba(255, 255, 255, 0)',
                'x': 0.18,
                'y': 0.90,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black'),

        )

    }
