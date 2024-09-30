from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from config import Config
import plotly.express as px
from dash import html
from layouts.map_layout import fig;

def map_callbacks(app):
        
    @app.callback(
    Output('world-map', 'figure'),
    Input('world-map', 'relayoutData')
    )
    def update_zoom(relayout_data):
        return fig