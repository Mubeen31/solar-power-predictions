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
from sklearn import metrics
from xgboost import XGBRegressor
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


def summary_value(n_intervals, select_trees, select_random_state):
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
    weather_data.drop(['Date', 'Time', 'DewPoint (°C)', 'Direction', 'Visibility (km)',
                       'UVIndexText', 'PreProbability (%)', 'RainProbability (%)', 'weather status', 'Hum (%)',
                       'CloudCover (%)', 'Temp (°C)'], axis = 1, inplace = True)

    df1 = pd.concat([daily_hourly_values, weather_data], axis = 1)
    df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
    df1.loc[df1['SolarIrradiance (W/m2)'] == 0, ['RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']] = 0

    filter_last_day_values = df[df['Date'] == unique_date[-2]][['Date', 'Hour', 'Power (KW)']]
    last_day_hourly_values = filter_last_day_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
    last_day_hourly_values_sum = last_day_hourly_values['Power (KW)'].sum()

    filter_yes_values = df[(df['Date'] >= '2022-06-25') & (df['Date'] <= unique_date[-3])][
        ['Date', 'Hour', 'Power (KW)']]
    yes_hourly_values = filter_yes_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
    header_list = ['Date', 'Time', 'SolarIrradiance (W/m2)', 'weather status', 'Temp (°C)', 'RealFeelTemp (°C)',
                   'DewPoint (°C)', 'Wind (km/h)',
                   'Direction', 'Hum (%)', 'Visibility (km)', 'UVIndex', 'UVIndexText', 'PreProbability (%)',
                   'RainProbability (%)',
                   'CloudCover (%)']
    weather_data1 = pd.read_csv('https://raw.githubusercontent.com/Mubeen31/solar-power-and-weather-data/main/hourly_weather_forecasted_data.csv', names = header_list, encoding = 'unicode_escape')
    weather_unique_date = weather_data1['Date'].unique()
    filter_weather_yes_values = weather_data1[
        (weather_data1['Date'] >= '2022-06-25') &
        (weather_data1['Date'] <= weather_unique_date[-3])][
        ['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']]
    yes_df1 = pd.concat([yes_hourly_values, filter_weather_yes_values], axis = 1)
    yes_df1.drop(['Date', 'Hour'], axis = 1, inplace = True)
    yes_df1.loc[yes_df1['SolarIrradiance (W/m2)'] == 0, ['RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']] = 0
    yes_count_total_rows = len(yes_df1)
    yes_independent_columns = yes_df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']][
                              0:yes_count_total_rows]
    yes_dependent_column = yes_df1['Power (KW)'][0:yes_count_total_rows]
    yes_reg = linear_model.LinearRegression(fit_intercept = False)
    yes_reg.fit(yes_independent_columns, yes_dependent_column)
    forcasted_yes_values = weather_data1[(weather_data1['Date'] == weather_unique_date[-2])][
        ['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']]
    forcasted_yes_values.loc[
        forcasted_yes_values['SolarIrradiance (W/m2)'] == 0, ['RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']] = 0
    return_array = yes_reg.predict(forcasted_yes_values)
    predicted_data = pd.DataFrame(return_array, columns = ['Power (KW)'])
    mv_pe = predicted_data['Power (KW)'].sum()
    mv_mse = metrics.mean_squared_error(last_day_hourly_values['Power (KW)'], predicted_data['Power (KW)'])
    mv_rmse = np.sqrt(mv_mse)
    mv_mae = metrics.mean_absolute_error(last_day_hourly_values['Power (KW)'], predicted_data['Power (KW)'])
    mv_rs = metrics.r2_score(last_day_hourly_values['Power (KW)'], predicted_data['Power (KW)'])

    rfr_yes = RandomForestRegressor(n_estimators = 100, random_state = 0)
    rfr_yes.fit(yes_independent_columns, yes_dependent_column)
    rfr_yes_return_array = rfr_yes.predict(forcasted_yes_values)
    rfr_yes_predicted_data = pd.DataFrame(rfr_yes_return_array, columns = ['Power (KW)'])
    rfr_yes_pe = rfr_yes_predicted_data['Power (KW)'].sum()
    rfr_yes_mse = metrics.mean_squared_error(last_day_hourly_values['Power (KW)'], rfr_yes_predicted_data['Power (KW)'])
    rfr_yes_rmse = np.sqrt(rfr_yes_mse)
    rfr_yes_mae = metrics.mean_absolute_error(last_day_hourly_values['Power (KW)'],
                                              rfr_yes_predicted_data['Power (KW)'])
    rfr_yes_rs = metrics.r2_score(last_day_hourly_values['Power (KW)'], rfr_yes_predicted_data['Power (KW)'])

    if time_name >= '00:00:00' and time_name <= '11:59:59':
        count_total_rows = len(df1) - 12
        independent_columns = df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']][
                              0:count_total_rows]
        dependent_column = df1['Power (KW)'][0:count_total_rows]

        reg = XGBRegressor(n_estimators=69, predictor = 'cpu_predictor')
        reg.fit(independent_columns, dependent_column)

        forcasted_data = df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']].tail(12)

        return_array = list(reg.predict(forcasted_data))

        date = now.strftime('%Y-%m-%d')
        current_date_12 = [date, date, date, date, date, date, date, date, date, date, date, date]

        hours_12 = list(daily_hourly_values['Hour'][0:12])

        data_dict = {'Date': current_date_12, 'Hour': hours_12, 'Power (KW)': return_array}

        data_dataframe = pd.DataFrame(data_dict)
        data_12 = data_dataframe['Power (KW)'].sum()

        filter_today_values = df[df['Date'] == unique_date[-1]][['Date', 'Hour', 'Power (KW)']]
        today_hourly_values = filter_today_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
        length_today_hourly_values = len(today_hourly_values)
        today_sum_12 = today_hourly_values['Power (KW)'].sum()

        mean_sq_error_12 = metrics.mean_squared_error(today_hourly_values['Power (KW)'],
                                                      data_dataframe['Power (KW)'].head(length_today_hourly_values))
        root_mean_sq_error_12 = np.sqrt(mean_sq_error_12)
        mean_ab_error_12 = metrics.mean_absolute_error(today_hourly_values['Power (KW)'],
                                                       data_dataframe['Power (KW)'].head(length_today_hourly_values))
        r_squared_12 = metrics.r2_score(today_hourly_values['Power (KW)'],
                                        data_dataframe['Power (KW)'].head(length_today_hourly_values))


    elif time_name >= '12:00:00' and time_name <= '23:59:59':
        count_total_rows = len(df1) - 24
        independent_columns = df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']][
                              0:count_total_rows]
        dependent_column = df1['Power (KW)'][0:count_total_rows]

        reg = XGBRegressor(n_estimators=69, predictor = 'cpu_predictor')
        reg.fit(independent_columns, dependent_column)

        forcasted_data = df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']].tail(24)

        return_array = list(reg.predict(forcasted_data))

        date = now.strftime('%Y-%m-%d')
        current_date_24 = [date, date, date, date, date, date, date, date, date, date, date, date, date, date, date,
                           date, date, date, date, date, date, date, date, date]

        hours_24 = list(daily_hourly_values['Hour'][0:24])

        data_dict = {'Date': current_date_24, 'Hour': hours_24, 'Power (KW)': return_array}

        data_dataframe = pd.DataFrame(data_dict)
        data_24 = data_dataframe['Power (KW)'].sum()

        filter_today_values = df[df['Date'] == unique_date[-1]][['Date', 'Hour', 'Power (KW)']]
        today_hourly_values = filter_today_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
        length_today_hourly_values = len(today_hourly_values)
        today_sum_24 = today_hourly_values['Power (KW)'].sum()

        mean_sq_error_24 = metrics.mean_squared_error(today_hourly_values['Power (KW)'],
                                                      data_dataframe['Power (KW)'].head(length_today_hourly_values))
        root_mean_sq_error_24 = np.sqrt(mean_sq_error_24)
        mean_ab_error_24 = metrics.mean_absolute_error(today_hourly_values['Power (KW)'],
                                                       data_dataframe['Power (KW)'].head(length_today_hourly_values))
        r_squared_24 = metrics.r2_score(today_hourly_values['Power (KW)'],
                                        data_dataframe['Power (KW)'].head(length_today_hourly_values))
    if time_name >= '00:00:00' and time_name <= '11:59:59':
        count_total_rows = len(df1) - 12
        independent_columns = df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']][
                              0:count_total_rows]
        dependent_column = df1['Power (KW)'][0:count_total_rows]

        rfr = RandomForestRegressor(n_estimators = select_trees, random_state = select_random_state)
        rfr.fit(independent_columns, dependent_column)

        forcasted_data = df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']].tail(12)

        return_array = list(rfr.predict(forcasted_data))

        date = now.strftime('%Y-%m-%d')
        current_date_12 = [date, date, date, date, date, date, date, date, date, date, date, date]

        hours_12 = list(daily_hourly_values['Hour'][0:12])

        data_dict = {'Date': current_date_12, 'Hour': hours_12, 'Power (KW)': return_array}

        data_dataframe = pd.DataFrame(data_dict)
        rn_data_12 = data_dataframe['Power (KW)'].sum()

        filter_today_values = df[df['Date'] == unique_date[-1]][['Date', 'Hour', 'Power (KW)']]
        today_hourly_values = filter_today_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
        length_today_hourly_values = len(today_hourly_values)
        rn_today_sum_12 = today_hourly_values['Power (KW)'].sum()

        rn_mean_sq_error_12 = metrics.mean_squared_error(today_hourly_values['Power (KW)'],
                                                         data_dataframe['Power (KW)'].head(length_today_hourly_values))
        rn_root_mean_sq_error_12 = np.sqrt(rn_mean_sq_error_12)
        rn_mean_ab_error_12 = metrics.mean_absolute_error(today_hourly_values['Power (KW)'],
                                                          data_dataframe['Power (KW)'].head(length_today_hourly_values))
        rn_r_squared_12 = metrics.r2_score(today_hourly_values['Power (KW)'],
                                           data_dataframe['Power (KW)'].head(length_today_hourly_values))

    elif time_name >= '12:00:00' and time_name <= '23:59:59':
        count_total_rows = len(df1) - 24
        independent_columns = df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']][
                              0:count_total_rows]
        dependent_column = df1['Power (KW)'][0:count_total_rows]

        rfr = RandomForestRegressor(n_estimators = select_trees, random_state = select_random_state)
        rfr.fit(independent_columns, dependent_column)

        forcasted_data = df1[['SolarIrradiance (W/m2)', 'RealFeelTemp (°C)', 'Wind (km/h)', 'UVIndex']].tail(24)

        return_array = list(rfr.predict(forcasted_data))

        date = now.strftime('%Y-%m-%d')
        current_date_24 = [date, date, date, date, date, date, date, date, date, date, date, date, date, date, date,
                           date, date, date, date, date, date, date, date, date]

        hours_24 = list(daily_hourly_values['Hour'][0:24])

        data_dict = {'Date': current_date_24, 'Hour': hours_24, 'Power (KW)': return_array}

        data_dataframe = pd.DataFrame(data_dict)
        rn_data_24 = data_dataframe['Power (KW)'].sum()

        filter_today_values = df[df['Date'] == unique_date[-1]][['Date', 'Hour', 'Power (KW)']]
        today_hourly_values = filter_today_values.groupby(['Date', 'Hour'])['Power (KW)'].sum().reset_index()
        length_today_hourly_values = len(today_hourly_values)
        rn_today_sum_24 = today_hourly_values['Power (KW)'].sum()

        rn_mean_sq_error_24 = metrics.mean_squared_error(today_hourly_values['Power (KW)'],
                                                         data_dataframe['Power (KW)'].head(length_today_hourly_values))
        rn_root_mean_sq_error_24 = np.sqrt(rn_mean_sq_error_24)
        rn_mean_ab_error_24 = metrics.mean_absolute_error(today_hourly_values['Power (KW)'],
                                                          data_dataframe['Power (KW)'].head(length_today_hourly_values))
        rn_r_squared_24 = metrics.r2_score(today_hourly_values['Power (KW)'],
                                           data_dataframe['Power (KW)'].head(length_today_hourly_values))

    if time_name >= '00:00:00' and time_name <= '11:59:59':
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.P('Today Results', className = 'stat_results'),
                        ]),
                    ], className = 'error_container1'),
                    html.Div([
                        html.Div([
                            html.P('PE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('AE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('MSE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('RMSE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('MAE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('R²', className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container2'),

                    html.Div([
                        html.Div([
                            html.P('Multivariable Linear Regression Model', className = 'error_text'),
                        ], className = 'error_bg1'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(data_12),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(today_sum_12),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mean_sq_error_12),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(root_mean_sq_error_12),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mean_ab_error_12),
                                   className = 'error_text')
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(r_squared_12),
                                   className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container3'),

                    html.Div([
                        html.Div([
                            html.P('Random Forest Regression Model', className = 'error_text'),
                        ], className = 'error_bg1'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(rn_data_12),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(rn_today_sum_12),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rn_mean_sq_error_12),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rn_root_mean_sq_error_12),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rn_mean_ab_error_12),
                                   className = 'error_text')
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rn_r_squared_12),
                                   className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container3')
                ], className = 'error_container_column'),

                html.Div([
                    html.Div([
                        html.Div([
                            html.P('Yesterday Results', className = 'stat_results'),
                        ]),
                    ], className = 'error_container1'),
                    html.Div([
                        html.Div([
                            html.P('PE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('AE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('MSE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('RMSE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('MAE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('R²', className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container2'),

                    html.Div([
                        html.Div([
                            html.P('Multivariable Linear Regression Model', className = 'error_text'),
                        ], className = 'error_bg1'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(mv_pe),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(last_day_hourly_values_sum),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mv_mse),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mv_rmse),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mv_mae),
                                   className = 'error_text')
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mv_rs),
                                   className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container3'),

                    html.Div([
                        html.Div([
                            html.P('Random Forest Regression Model', className = 'error_text'),
                        ], className = 'error_bg1'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(rfr_yes_pe),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(last_day_hourly_values_sum),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rfr_yes_mse),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rfr_yes_rmse),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rfr_yes_mae),
                                   className = 'error_text')
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rfr_yes_rs),
                                   className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container3')
                ], className = 'error_container_column')
            ], className = 'results_column')
        ]
    elif time_name >= '12:00:00' and time_name <= '23:59:59':
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.P('Today Results', className = 'stat_results'),
                        ]),
                    ], className = 'error_container1'),
                    html.Div([
                        html.Div([
                            html.P('PE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('AE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('MSE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('RMSE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('MAE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('R²', className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container2'),

                    html.Div([
                        html.Div([
                            html.P('Multivariable Linear Regression Model', className = 'error_text'),
                        ], className = 'error_bg1'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(data_24),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(today_sum_24),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mean_sq_error_24),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(root_mean_sq_error_24),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mean_ab_error_24),
                                   className = 'error_text')
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(r_squared_24),
                                   className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container3'),

                    html.Div([
                        html.Div([
                            html.P('Random Forest Regression Model', className = 'error_text'),
                        ], className = 'error_bg1'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(rn_data_24),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(rn_today_sum_24),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rn_mean_sq_error_24),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rn_root_mean_sq_error_24),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rn_mean_ab_error_24),
                                   className = 'error_text')
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rn_r_squared_24),
                                   className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container3')
                ], className = 'error_container_column'),

                html.Div([
                    html.Div([
                        html.Div([
                            html.P('Yesterday Results', className = 'stat_results'),
                        ]),
                    ], className = 'error_container1'),
                    html.Div([
                        html.Div([
                            html.P('PE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('AE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('MSE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('RMSE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('MAE', className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('R²', className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container2'),

                    html.Div([
                        html.Div([
                            html.P('Multivariable Linear Regression Model', className = 'error_text'),
                        ], className = 'error_bg1'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(mv_pe),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(last_day_hourly_values_sum),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mv_mse),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mv_rmse),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mv_mae),
                                   className = 'error_text')
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(mv_rs),
                                   className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container3'),

                    html.Div([
                        html.Div([
                            html.P('Random Forest Regression Model', className = 'error_text'),
                        ], className = 'error_bg1'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(rfr_yes_pe),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.2f} KWh'.format(last_day_hourly_values_sum),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rfr_yes_mse),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rfr_yes_rmse),
                                   className = 'error_text'),
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rfr_yes_mae),
                                   className = 'error_text')
                        ], className = 'error_bg'),
                        html.Div([
                            html.P('{0:,.4f}'.format(rfr_yes_rs),
                                   className = 'error_text')
                        ], className = 'error_bg')
                    ], className = 'error_container3')
                ], className = 'error_container_column')
            ], className = 'results_column')
        ]
