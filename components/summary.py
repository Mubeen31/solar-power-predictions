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


def summary_value(n_intervals, select_trees, select_random_state):
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
                        html.P('16.99 KWh',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('MAE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg')
                ], className = 'error_container3'),

                html.Div([
                    html.Div([
                        html.P('Support Vector Regression Model', className = 'error_text'),
                    ], className = 'error_bg1'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('MAE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg')
                ], className = 'error_container3'),

                html.Div([
                    html.Div([
                        html.P('Random Forest Regression Model', className = 'error_text'),
                    ], className = 'error_bg1'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('MAE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
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
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('MAE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg')
                ], className = 'error_container3'),

                html.Div([
                    html.Div([
                        html.P('Support Vector Regression Model', className = 'error_text'),
                    ], className = 'error_bg1'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('MAE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg')
                ], className = 'error_container3'),

                html.Div([
                    html.Div([
                        html.P('Random Forest Regression Model', className = 'error_text'),
                    ], className = 'error_bg1'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('RMSE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('MAE',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text'),
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg'),
                    html.Div([
                        html.P('R²',
                               # html.P('{0:,.5f}'.format(energy_kilo_watts)),
                               className = 'error_text')
                    ], className = 'error_bg')
                ], className = 'error_container3')
            ], className = 'error_container_column')
        ], className = 'results_column')
    ]
