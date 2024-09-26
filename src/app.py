import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from layouts.main_layout import create_main_layout, about_layout, home_layout
from layouts.map_layout import create_map_layout
from callbacks.map_callbacks import register_callbacks

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='viewport-size', style={'display': 'none'}),  # Hidden div to store the viewport size
    create_map_layout()
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    match pathname:
        case '/carte':
            return create_map_layout()
        case '/about':
            return about_layout()
        case _:
            return home_layout()

app.clientside_callback(
    """
    function(href) {
        return JSON.stringify({'height': window.innerHeight, 'width': window.innerWidth});
    }
    """,
    Output('viewport-size', 'children'),
    Input('url', 'href')
)


register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
