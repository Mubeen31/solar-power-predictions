import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime
from components.last_data_update_time import last_data_update_time_value
# from components.header import header_value
from components.solar_first_card import solar_first_card_value
from components.solar_second_card import solar_second_card_value
from components.energy_forcasting_card import energy_forcasting_card_value
from components.solar_third_card import solar_third_card_value
from components.solar_fourth_card import solar_fourth_card_value
from components.solar_fifth_card import solar_fifth_card_value
from components.solar_current_power_chart import solar_current_power_chart_value
from components.solar_today_power_chart import solar_today_power_chart_value
from components.solar_yesterday_power_chart import solar_yesterday_power_chart_value
from components.energy_forecasting import energy_forecasting_chart_value
from components.random_forest_regression import random_forest_regression_chart_value
from components.current_weather import current_weather_value
from components.first_hour_forecast import first_hour_forecast_weather_value
from components.second_hour_forecast import second_hour_forecast_weather_value
from components.third_hour_forecast import third_hour_forecast_weather_value

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server
app.title = 'Solar Energy Predictions'

tabs_styles = {
    "flex-direction": "row",
}
tab_style = {
    "padding": "0vh",
    "color": '#1a1a1a',
    "font-family": "Calibri",
    "font-size": "16px",
    "backgroundColor": '#d9d9d9',
    # 'border-bottom': '2px #FF0000 solid',
    'border-left': '2px #ffffff solid',
    # 'width': '120px',
}

tab_style1 = {
    "padding": "0vh",
    "color": '#1a1a1a',
    "font-family": "Calibri",
    "font-size": "16px",
    "backgroundColor": '#d9d9d9',
    # 'border-bottom': '2px #FF0000 solid',
    # 'width': '120px',
}

tab_selected_style = {
    "color": '#FF0000',
    "font-family": "Calibri",
    "font-size": "16px",
    "padding": "0vh",
    "backgroundColor": 'rgb(255, 255, 255)',
    # 'width': '120px',
}

solar_current_power_chart = dcc.Graph(id = 'solar_current_power_chart',
                                      animate = True,
                                      config = {'displayModeBar': False},
                                      className = 'background2')
solar_today_power_chart = dcc.Graph(id = 'solar_today_power_chart',
                                    animate = True,
                                    config = {'displayModeBar': False},
                                    className = 'background2')
solar_yesterday_power_chart = dcc.Graph(id = 'solar_yesterday_power_chart',
                                        animate = True,
                                        config = {'displayModeBar': False},
                                        className = 'background2')
energy_forcasting_chart = dcc.Graph(id = 'energy_forcasting_chart',
                                    animate = True,
                                    config = {'displayModeBar': False},
                                    className = 'background2')
support_vector_regression_chart = dcc.Graph(id = 'support_vector_regression_chart',
                                            animate = True,
                                            config = {'displayModeBar': False},
                                            className = 'background2')
random_forest_regression_chart = dcc.Graph(id = 'random_forest_regression_chart',
                                           animate = True,
                                           config = {'displayModeBar': False},
                                           className = 'background2')
summary = html.Div(id = 'summary',
                   className = 'background2')

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src = app.get_asset_url('solar-panel.png'),
                     style = {'height': '30px'},
                     className = 'title_image'
                     ),
            html.H6('Solar Energy Predictions',
                    style = {'color': '#1a1a1a'},
                    className = 'title'
                    ),
        ], className = 'logo_title'),
        html.P(id = 'last_data_update_time',
               style = {'color': '#eb6e4b'},
               className = 'adjust_date_time'
               ),
        # html.P(id = 'get_date_time',
        #        style = {'color': '#eb6e4b'},
        #        className = 'adjust_date_time'
        #        )
    ], className = 'title_date_time_container'),
    html.Div([
        dcc.Interval(id = 'update_time',
                     interval = 1000,
                     n_intervals = 0),
    ]),
    html.Div([
        dcc.Interval(id = 'update_date_time_value',
                     interval = 60000,
                     n_intervals = 0),
    ]),
    html.Div([
        dcc.Interval(id = 'solar_energy_forcasting_card',
                     interval = 10000,
                     n_intervals = 0),
    ]),

    html.Div([
        html.Div([
            html.Div([
                html.Div(id = 'solar_first_card')
            ], className = 'adjust_card'),
            html.Div([
                html.Div(id = 'solar_second_card')
            ], className = 'adjust_card'),
            html.Div([
                html.Div(id = 'solar_third_card')
            ], className = 'adjust_card'),
            html.Div([
                html.Div(id = 'solar_fourth_card')
            ], className = 'adjust_card'),
            html.Div([
                html.Div(id = 'solar_fifth_card')
            ], className = 'adjust_last_card'),
        ], className = 'background1')
    ], className = 'adjust_margin1'),
    html.Div([
        html.Div([
            dcc.Tabs(value = 'energy_forcasting_chart', children = [
                dcc.Tab(solar_current_power_chart,
                        label = 'Current Power',
                        value = 'solar_current_power_chart',
                        style = tab_style1,
                        selected_style = tab_selected_style,
                        ),
                dcc.Tab(solar_today_power_chart,
                        label = 'Today Energy',
                        value = 'solar_today_power_chart',
                        style = tab_style,
                        selected_style = tab_selected_style,
                        ),
                dcc.Tab(solar_yesterday_power_chart,
                        label = 'Yesterday Energy',
                        value = 'solar_yesterday_power_chart',
                        style = tab_style,
                        selected_style = tab_selected_style,
                        ),
                dcc.Tab(energy_forcasting_chart,
                        label = 'MVLR Model',
                        value = 'energy_forcasting_chart',
                        style = tab_style,
                        selected_style = tab_selected_style,
                        ),
                dcc.Tab(support_vector_regression_chart,
                        label = 'SVR Model',
                        value = 'support_vector_regression_chart',
                        style = tab_style,
                        selected_style = tab_selected_style,
                        ),
                dcc.Tab(random_forest_regression_chart,
                        label = 'RFR Model',
                        value = 'random_forest_regression_chart',
                        style = tab_style,
                        selected_style = tab_selected_style,
                        ),
                dcc.Tab(summary,
                        label = 'Summary',
                        value = 'summary',
                        style = tab_style,
                        selected_style = tab_selected_style,
                        ),
            ], style = tabs_styles,
                     colors = {"border": None,
                               "primary": None,
                               "background": None}),
        ], className = 'tabs'),
        html.Div([
            html.Div([
                html.Div([
                    html.H6('Worcester, GB', className = 'title_city'),
                    html.Div(id = 'current_weather')
                ], className = 'weather1'),
                html.Div([
                    html.Div([
                        html.Div(id = 'first_hour_forecast'),
                        html.Div(id = 'second_hour_forecast'),
                        html.Div(id = 'third_hour_forecast')
                    ], className = 'forecast_cards_row'),
                ], className = 'weather2')
            ], className = 'weather_column')
        ], className = 'weather_background')
    ], className = 'adjust_margin2'),
])


@app.callback(Output('last_data_update_time', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def last_data_update_time_value_callback(n_intervals):
    last_data_update_time_value_data = last_data_update_time_value(n_intervals)

    return last_data_update_time_value_data


# @app.callback(Output('get_date_time', 'children'),
#               [Input('update_time', 'n_intervals')])
# def header_value_callback(n_intervals):
#     header_value_data = header_value(n_intervals)
#
#     return header_value_data


@app.callback(Output('solar_first_card', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_first_card_value_callback(n_intervals):
    solar_first_card_value_data = solar_first_card_value(n_intervals)

    return solar_first_card_value_data


@app.callback(Output('solar_second_card', 'children'),
              [Input('solar_energy_forcasting_card', 'n_intervals')])
def solar_energy_forcasting_second_card_value_callback(n_intervals):
    if n_intervals == None or n_intervals % 2 == 1:
        solar_energy_forcasting_second_card_value_data = solar_second_card_value(n_intervals)
    elif n_intervals % 2 == 0:
        solar_energy_forcasting_second_card_value_data = energy_forcasting_card_value(n_intervals)
    else:
        solar_energy_forcasting_second_card_value_data = "None"

    return solar_energy_forcasting_second_card_value_data


@app.callback(Output('solar_third_card', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_third_card_value_callback(n_intervals):
    solar_third_card_value_data = solar_third_card_value(n_intervals)

    return solar_third_card_value_data


@app.callback(Output('solar_fourth_card', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_fourth_card_value_callback(n_intervals):
    solar_fourth_card_value_data = solar_fourth_card_value(n_intervals)

    return solar_fourth_card_value_data


@app.callback(Output('solar_fifth_card', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_fifth_card_value_callback(n_intervals):
    solar_fifth_card_value_data = solar_fifth_card_value(n_intervals)

    return solar_fifth_card_value_data


@app.callback(Output('solar_current_power_chart', 'figure'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_current_power_chart_value_callback(n_intervals):
    solar_current_power_chart_value_data = solar_current_power_chart_value(n_intervals)

    return solar_current_power_chart_value_data


@app.callback(Output('solar_today_power_chart', 'figure'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_today_power_chart_value_callback(n_intervals):
    solar_today_power_chart_value_data = solar_today_power_chart_value(n_intervals)

    return solar_today_power_chart_value_data


@app.callback(Output('solar_yesterday_power_chart', 'figure'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_yesterday_power_chart_value_callback(n_intervals):
    solar_yesterday_power_chart_value_data = solar_yesterday_power_chart_value(n_intervals)

    return solar_yesterday_power_chart_value_data


@app.callback(Output('energy_forcasting_chart', 'figure'),
              [Input('update_date_time_value', 'n_intervals')])
def energy_forecasting_chart_value_callback(n_intervals):
    energy_forecasting_chart_value_data = energy_forecasting_chart_value(n_intervals)

    return energy_forecasting_chart_value_data


@app.callback(Output('random_forest_regression_chart', 'figure'),
              [Input('update_date_time_value', 'n_intervals')])
def random_forest_regression_chart_value_callback(n_intervals):
    random_forest_regression_chart_value_data = random_forest_regression_chart_value(n_intervals)

    return random_forest_regression_chart_value_data


@app.callback(Output('current_weather', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def current_weather_value_callback(n_intervals):
    current_weather_value_data = current_weather_value(n_intervals)

    return current_weather_value_data


# @app.callback(Output('forecast_weather', 'children'),
#               [Input('update_forecast_value', 'n_intervals')])
# def forecast_weather_value_callback(n_intervals):
#     if n_intervals == None or n_intervals % 2 == 1:
#         forecast_weather_value_data = forecast_weather_value(n_intervals)
#     elif n_intervals % 2 == 0:
#         forecast_weather_value_data = forecast_weather2_value(n_intervals)
#     else:
#         forecast_weather_value_data = "None"
#     return forecast_weather_value_data

@app.callback(Output('first_hour_forecast', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def first_hour_forecast_value_callback(n_intervals):
    first_hour_forecast_value_data = first_hour_forecast_weather_value(n_intervals)

    return first_hour_forecast_value_data


@app.callback(Output('second_hour_forecast', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def second_hour_forecast_value_callback(n_intervals):
    second_hour_forecast_value_data = second_hour_forecast_weather_value(n_intervals)

    return second_hour_forecast_value_data


@app.callback(Output('third_hour_forecast', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def third_hour_forecast_value_callback(n_intervals):
    third_hour_forecast_value_data = third_hour_forecast_weather_value(n_intervals)

    return third_hour_forecast_value_data


if __name__ == "__main__":
    app.run_server(debug = True)
