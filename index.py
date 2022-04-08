import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime
from components.header import header_value

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

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
        dcc.Interval(id = 'update_date_time',
                     interval = 1000,
                     n_intervals = 0),
    ]),
    html.Div([
            html.Div([
                html.Div([
                ], className = 'adjust_card'),
                html.Div([
                ], className = 'adjust_card'),
                html.Div([
                ], className = 'adjust_card'),
                html.Div([
                ], className = 'adjust_card'),
                html.Div([
                ], className = 'adjust_last_card'),
            ], className = 'background')
    ], className = 'adjust_margin'),
])


@app.callback(Output('get_date_time', 'children'),
              [Input('update_date_time', 'n_intervals')])
def header_value_callback(n_intervals):
    header_value_data = header_value(n_intervals)

    return header_value_data


if __name__ == "__main__":
    app.run_server(debug = True)
