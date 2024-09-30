from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from config import Config
import plotly.express as px
from dash import html


def overlay_layout(app):
    @app.callback(
    Output('Title_graph', 'children'),
    Input('world-map', 'clickData')
    )
    def change_title_upon_selection(clickData):
        if clickData:
            print(clickData)
            return f"Perception of India in {clickData['points'][0]['location']}"
        else:
            return f"Perception of India in World"

