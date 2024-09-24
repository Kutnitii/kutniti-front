from dash import html, dcc

def create_map_layout():
    return html.Div([
        html.Div(id="sidebar", className="sidebar", children=[
            html.H3("Country information"),
            html.Div(id='details-pays', children=[
                html.P("Click on a country to see some details.")
            ]),
            dcc.Graph(id='additional-graph', config={'displayModeBar': False}, style={'display': 'none'}),
            html.P("Click on a country to see some details."),
            dcc.Graph(id='sentiment-bar', config={'displayModeBar': False, 'staticPlot': True}, style={'display': 'none'}),
            html.P("Click on a country to see some details.")
        ]),
        dcc.Graph(id='carte-monde', config={'displayModeBar': False}),
    ], className='map-container')
