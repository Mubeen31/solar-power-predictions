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
# from xgboost import XGBRegressor
import sqlalchemy
from dash import dash_table as dt
import time
from components.select_date import training_dataset_date
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


def solar_yesterday_power_chart_value(n_intervals):
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
    df['time'] = pd.to_datetime(df['DateTime']).dt.time
    df['hour'] = pd.to_datetime(df['DateTime']).dt.hour
    df['time'].iloc[-1].strftime('%H:%M')
    df['time'] = df['time'].astype(str)
    df['hour'] = df['hour'].astype(str)
    df['Time'] = pd.to_datetime(df['DateTime']).dt.time
    df['Hour'] = pd.to_datetime(df['DateTime']).dt.hour
    df['Time'] = df['Time'].astype(str)
    today_date = df['Date'].unique()

    first_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '00:00:00') & (df['time'] <= '00:59:59')]
    first_hour_energy = first_hour['Power (KW)'].sum()

    second_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '01:00:00') & (df['time'] <= '01:59:59')]
    second_hour_energy = second_hour['Power (KW)'].sum()

    third_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '02:00:00') & (df['time'] <= '02:59:59')]
    third_hour_energy = third_hour['Power (KW)'].sum()

    fourth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '03:00:00') & (df['time'] <= '03:59:59')]
    fourth_hour_energy = fourth_hour['Power (KW)'].sum()

    fifth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '04:00:00') & (df['time'] <= '04:59:59')]
    fifth_hour_energy = fifth_hour['Power (KW)'].sum()

    sixth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '05:00:00') & (df['time'] <= '05:59:59')]
    sixth_hour_energy = sixth_hour['Power (KW)'].sum()

    seventh_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '06:00:00') & (df['time'] <= '06:59:59')]
    seventh_hour_energy = seventh_hour['Power (KW)'].sum()

    eighth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '07:00:00') & (df['time'] <= '07:59:59')]
    eighth_hour_energy = eighth_hour['Power (KW)'].sum()

    nineth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '08:00:00') & (df['time'] <= '08:59:59')]
    nineth_hour_energy = nineth_hour['Power (KW)'].sum()

    tenth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '09:00:00') & (df['time'] <= '09:59:59')]
    tenth_hour_energy = tenth_hour['Power (KW)'].sum()

    eleventh_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '10:00:00') & (df['time'] <= '10:59:59')]
    eleventh_hour_energy = eleventh_hour['Power (KW)'].sum()

    twelth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '11:00:00') & (df['time'] <= '11:59:59')]
    twelth_hour_energy = twelth_hour['Power (KW)'].sum()

    thirteenth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '12:00:00') & (df['time'] <= '12:59:59')]
    thirteenth_hour_energy = thirteenth_hour['Power (KW)'].sum()

    fourteenth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '13:00:00') & (df['time'] <= '13:59:59')]
    fourteenth_hour_energy = fourteenth_hour['Power (KW)'].sum()

    fifteenth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '14:00:00') & (df['time'] <= '14:59:59')]
    fifteenth_hour_energy = fifteenth_hour['Power (KW)'].sum()

    sixteenth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '15:00:00') & (df['time'] <= '15:59:59')]
    sixteenth_hour_energy = sixteenth_hour['Power (KW)'].sum()

    seventeenth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '16:00:00') & (df['time'] <= '16:59:59')]
    seventeenth_hour_energy = seventeenth_hour['Power (KW)'].sum()

    eighteenth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '17:00:00') & (df['time'] <= '17:59:59')]
    eighteenth_hour_energy = eighteenth_hour['Power (KW)'].sum()

    nineteenth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '18:00:00') & (df['time'] <= '18:59:59')]
    nineteenth_hour_energy = nineteenth_hour['Power (KW)'].sum()

    twenteeth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '19:00:00') & (df['time'] <= '19:59:59')]
    twenteeth_hour_energy = twenteeth_hour['Power (KW)'].sum()

    twentyoneth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '20:00:00') & (df['time'] <= '20:59:59')]
    twentyoneth_hour_energy = twentyoneth_hour['Power (KW)'].sum()

    twentysecond_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '21:00:00') & (df['time'] <= '21:59:59')]
    twentysecond_hour_energy = twentysecond_hour['Power (KW)'].sum()

    twentythird_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '22:00:00') & (df['time'] <= '22:59:59')]
    twentythird_hour_energy = twentythird_hour['Power (KW)'].sum()

    twentyfourth_hour = df[(df['Date'] == today_date[-2]) & (df['time'] >= '23:00:00') & (df['time'] <= '23:59:59')]
    twentyfourth_hour_energy = twentyfourth_hour['Power (KW)'].sum()

    hourly_data = [first_hour_energy, second_hour_energy, third_hour_energy, fourth_hour_energy, fifth_hour_energy,
                   sixth_hour_energy, seventh_hour_energy, eighth_hour_energy, nineth_hour_energy, tenth_hour_energy,
                   eleventh_hour_energy, twelth_hour_energy, thirteenth_hour_energy, fourteenth_hour_energy,
                   fifteenth_hour_energy, sixteenth_hour_energy, seventeenth_hour_energy, eighteenth_hour_energy,
                   nineteenth_hour_energy, twenteeth_hour_energy, twentyoneth_hour_energy, twentysecond_hour_energy,
                   twentythird_hour_energy, twentyfourth_hour_energy]
    hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    hourly_data_and_hours = {'Hours': hours, 'Hourly Data': hourly_data}
    hourly_data_and_hours_df = pd.DataFrame(hourly_data_and_hours)

    rearrange_columns = ['DateTime', 'Date', 'Time', 'Hour', 'Voltage', 'ValueCurrent', 'Power (W)', 'Power (KW)']
    df = df[rearrange_columns]
    unique_date = df['Date'].unique()
    # filter_daily_values = df[(df['Date'] > '2022-08-11') & (df['Date'] <= unique_date[-2])][
    #     ['Date', 'Hour', 'Power (KW)']]
    # daily_hourly_values = filter_daily_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
    #
    # header_list = ['Date', 'Time', 'SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
    #                'DewPoint (°C)',
    #                'Wind (km/h)',
    #                'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
    #                'RainProbability (%)',
    #                'CloudCover (%)']
    # weather_data = pd.read_csv(
    #     'https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/hourly_weather_forecasted_data.csv',
    #     names = header_list,
    #     encoding = 'unicode_escape')
    # weather_data['UV Index Text'] = pd.factorize(weather_data['UVIndexText'])[0]
    # weather_data.drop(['Date', 'Time', 'Direction', 'Visibility (km)',
    #                    'UVIndexText', 'PreProbability (%)', 'RainProbability (%)', 'weather status',
    #                    'CloudCover (%)', 'Hum (%)', 'DewPoint (°C)'], axis = 1,
    #                   inplace = True)
    #
    # df1 = pd.concat([daily_hourly_values, weather_data], axis = 1)
    # df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
    # df1.loc[df1['SolarIrradiance (W/m2)'] == 0, ['Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']] = 0

    filter_last_day_values = df[df['Date'] == unique_date[-2]][['Date', 'Hour', 'Power (KW)']]
    last_day_hourly_values = filter_last_day_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
    last_day_hourly_values_sum = last_day_hourly_values['Power (KW)'].sum()

    filter_yes_values = df[(df['Date'] >= training_dataset_date) & (df['Date'] <= unique_date[-3])][
        ['Date', 'Hour', 'Power (KW)']]
    yes_hourly_values = filter_yes_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
    header_list = ['Date', 'Time', 'SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
                   'DewPoint (°C)', 'Wind (km/h)',
                   'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
                   'RainProbability (%)',
                   'CloudCover (%)']
    weather_data1 = pd.read_csv(
        'https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/hourly_weather_forecasted_data.csv',
        names = header_list, encoding = 'unicode_escape')
    weather_data1['UV Index Text'] = pd.factorize(weather_data1['UVIndexText'])[0]
    weather_data1.loc[
        weather_data1['SolarIrradiance (W/m2)'] == 0, ['Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
                                                       'UV Index Text']] = 0
    weather_unique_date = weather_data1['Date'].unique()
    filter_weather_yes_values = \
        weather_data1[(weather_data1['Date'] >= training_dataset_date) & (weather_data1['Date'] <= weather_unique_date[-3])][
            ['Date', 'SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex',
             'UV Index Text']].reset_index()
    filter_weather_yes_values.drop(['index'], axis = 1, inplace = True)

    yes_df1 = pd.concat([yes_hourly_values, filter_weather_yes_values], axis = 1)
    yes_df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
    yes_count_total_rows = len(yes_df1)
    yes_independent_columns = yes_df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']][
                              0:yes_count_total_rows]
    yes_independent_columns1 = yes_df1[['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']][
                               0:yes_count_total_rows]
    yes_dependent_column = yes_df1['Power (KW)'][0:yes_count_total_rows]
    # yes_reg = XGBRegressor(n_estimators=69, predictor = 'cpu_predictor')
    # yes_reg.fit(yes_independent_columns, yes_dependent_column)
    forcasted_yes_values = weather_data1[(weather_data1['Date'] == weather_unique_date[-2])][
        ['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']]
    forcasted_yes_values1 = weather_data1[(weather_data1['Date'] == weather_unique_date[-2])][
        ['SolarIrradiance (W/m2)', 'Temp (°C)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex', 'UV Index Text']]
    # return_array = yes_reg.predict(forcasted_yes_values)
    # predicted_data = pd.DataFrame(return_array, columns = ['Power (KW)'])

    rfr_yes = RandomForestRegressor(n_estimators = 100, random_state = 0)
    rfr_yes.fit(yes_independent_columns1, yes_dependent_column)
    rfr_yes_return_array = rfr_yes.predict(forcasted_yes_values1)
    rfr_yes_predicted_data = pd.DataFrame(rfr_yes_return_array, columns = ['Power (KW)'])

    df3 = pd.read_csv('xgboost model/yesterday_predicted_chart_data.csv')

    return {
        'data': [go.Scatter(
            x = hourly_data_and_hours_df['Hours'],
            y = hourly_data_and_hours_df['Hourly Data'],
            name = 'Yesterday Solar Energy',
            mode = 'lines',
            marker = dict(color = '#4DBFF1'),
            hoverinfo = 'text',
            hovertext =
            '<b>Hour</b>: ' + hourly_data_and_hours_df['Hours'].astype(str) + '<br>' +
            '<b>Yesterday Solar Energy</b>: ' + [f'{x:,.5f} KWh' for x in
                                                 hourly_data_and_hours_df['Hourly Data']] + '<br>'
        ),
            go.Scatter(
                x = hourly_data_and_hours_df['Hours'],
                y = df3['Power (KW)'],
                name = 'Yesterday Predicted Solar Energy (XGBR Model)',
                mode = 'lines',
                line = dict(color = 'firebrick', dash = 'dash'),
                hoverinfo = 'text',
                hovertext =
                '<b>Hour</b>: ' + hourly_data_and_hours_df['Hours'].astype(str) + '<br>' +
                '<b>Yesterday Predicted Solar Energy (XGBR Model)</b>: ' + [f'{x:,.5f} KWh' for x in
                                                                            df3['Power (KW)']] + '<br>'
            ),
            go.Scatter(
                x = hourly_data_and_hours_df['Hours'],
                y = rfr_yes_predicted_data['Power (KW)'],
                name = 'Yesterday Predicted Solar Energy (RFR Model)',
                mode = 'lines',
                line = dict(color = '#FF7F50', dash = 'dot'),
                hoverinfo = 'text',
                hovertext =
                '<b>Hour</b>: ' + hourly_data_and_hours_df['Hours'].astype(str) + '<br>' +
                '<b>Yesterday Predicted Solar Energy (RFR Model)</b>: ' + [f'{x:,.5f} KWh' for x in
                                                                           rfr_yes_predicted_data[
                                                                               'Power (KW)']] + '<br>'
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
                'orientation': 'h',
                'bgcolor': 'rgba(255, 255, 255, 0)',
                'x': 0.5,
                'y': 1.2,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black'),

        )

    }
