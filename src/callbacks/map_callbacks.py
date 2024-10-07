from dash.dependencies import Input, Output
import dash
from layouts.map_layout import create_figure;

def map_callbacks(app):
    # Initialize a variable to store the last slider value
    last_slider_value = [0,100]  # Set a default value

    @app.callback(
        Output('world-map', 'figure'),
        [Input('world-map', 'relayoutData'), Input('my-slider', 'value')],
        prevent_initial_call=True
    )
    def update_map_and_zoom(relayout_data, slider_value):
        nonlocal last_slider_value

        ctx = dash.callback_context

        if not ctx.triggered:
            raise dash.exceptions.PreventUpdate

        trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigger_id == 'my-slider':
            last_slider_value = slider_value  
            return create_figure(last_slider_value[0],last_slider_value[1])

        elif trigger_id == 'world-map':
            return create_figure(last_slider_value[0],last_slider_value[1])

        raise dash.exceptions.PreventUpdate