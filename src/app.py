import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from layouts.main_layout import create_main_layout, about_layout, home_layout
from layouts.map_layout import create_map_layout
from callbacks.map_callbacks import register_callbacks
from callbacks.socials_callbacks import social_callback

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = create_main_layout()

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    match pathname:
        case '/map':
            return create_map_layout()
        case '/about':
            return about_layout()
        case _:
            return home_layout()

register_callbacks(app)
social_callback(app)


if __name__ == '__main__':
    app.run_server(debug=True)
