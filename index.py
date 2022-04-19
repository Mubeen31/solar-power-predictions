import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime
from components.header import header_value
from components.solar_first_card import solar_first_card_value
from components.solar_second_card import solar_second_card_value

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

tabs_styles = {
    "flex-direction": "row",
}
tab_style = {
    "padding": "0vh",
    "color": '#1a1a1a',
    "font-family": "Calibri",
    "font-size": "16px",
    "backgroundColor": 'rgb(255, 255, 255)',
    'width': '120px',
}

tab_selected_style = {
    "color": '#FF0000',
    "font-family": "Calibri",
    "font-size": "16px",
    "padding": "0vh",
    "backgroundColor": 'rgb(255, 255, 255)',
    'border-bottom': '2px #FF0000 solid',
    'width': '120px',
}

current_power = html.P('Current Power', className = 'background2')
today_power = html.P('Today Power', className = 'background2')
yesterday_power = html.P('Yesterday Power', className = 'background2')

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src = app.get_asset_url('solar-panel.png'),
                     style = {'height': '30px'},
                     className = 'title_image'
                     ),
            html.H6('Solar Power Predictions',
                    style = {'color': '#1a1a1a'},
                    className = 'title'
                    ),
        ], className = 'logo_title'),
        html.H6(id = 'get_date_time',
                style = {'color': '#1a1a1a'},
                className = 'adjust_date_time'
                )
    ], className = 'title_date_time_container'),
    html.Div([
        dcc.Interval(id = 'update_date_time_value',
                     interval = 1000,
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
            ], className = 'adjust_card'),
            html.Div([
            ], className = 'adjust_card'),
            html.Div([
            ], className = 'adjust_last_card'),
        ], className = 'background1')
    ], className = 'adjust_margin1'),
    html.Div([
        html.Div([
            dcc.Tabs(value = 'today_power', children = [
                dcc.Tab(current_power,
                        label = 'Current Power',
                        value = 'current_power',
                        style = tab_style,
                        selected_style = tab_selected_style,
                        ),
                dcc.Tab(today_power,
                        label = 'Today Power',
                        value = 'today_power',
                        style = tab_style,
                        selected_style = tab_selected_style,
                        ),
                dcc.Tab(yesterday_power,
                        label = 'Yesterday Power',
                        value = 'yesterday_power',
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
                ], className = 'weather1'),
                html.Div([
                ], className = 'weather2')
            ], className = 'weather_column')
        ], className = 'weather_background')
    ], className = 'adjust_margin2'),
])


@app.callback(Output('get_date_time', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def header_value_callback(n_intervals):
    header_value_data = header_value(n_intervals)

    return header_value_data


@app.callback(Output('solar_first_card', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_first_card_value_callback(n_intervals):
    solar_first_card_value_data = solar_first_card_value(n_intervals)

    return solar_first_card_value_data


@app.callback(Output('solar_second_card', 'children'),
              [Input('update_date_time_value', 'n_intervals')])
def solar_second_card_value_callback(n_intervals):
    solar_second_card_value_data = solar_second_card_value(n_intervals)

    return solar_second_card_value_data


if __name__ == "__main__":
    app.run_server(debug = True)
