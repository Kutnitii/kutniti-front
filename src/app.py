import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from layouts.main_layout import create_main_layout, about_layout
from layouts.map_layout import create_map_layout
from layouts.overlay_layout import create_overlayout
from callbacks.map_callbacks import map_callbacks
from callbacks.socials_callbacks import social_callback
from callbacks.overlay_callbacks import overlay_layout

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = create_main_layout()

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    match pathname:
        case '/main':
            return create_main_layout()
        case '/about':
            return about_layout()
        case _:
            return html.Div([
                create_map_layout(),
                create_overlayout()
            ])

map_callbacks(app)
social_callback(app)
overlay_layout(app)

if __name__ == '__main__':
    app.run_server(debug=True)
