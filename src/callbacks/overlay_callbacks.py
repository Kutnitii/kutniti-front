from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from config import Config
import plotly.express as px
from dash import html
from layouts.overlay_layout import create_overlayout;
from utils.data_processing import data_world_sunbrust;

def overlay_layout(app):
    @app.callback(
    Output('content_overlay', 'children'),
    Input('world-map', 'clickData')
    )
    def update_overlay(clickData):
        if (clickData):
            return create_overlayout(clickData['points'][0]['location'])
        return create_overlayout()



