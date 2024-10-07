from dash.dependencies import Input, Output
from layouts.overlay_layout import create_overlayout;
from dash import callback_context
def overlay_callbacks(app):
    @app.callback(
    Output('content_overlay', 'children'),
    Input('world-map', 'clickData')
    )
    def update_overlay(clickData):
        if (clickData):
            return create_overlayout(clickData['points'][0]['location'])
        return create_overlayout()