import dash
from dash import html
from dash.dependencies import Input, Output


def social_callbacks(app):
    
    @app.callback(
    Output('url', 'href', allow_duplicate=True),
    Input('twitter-button', 'n_clicks'),
    prevent_initial_call=True
    )
    def go_to_x(n_clicks):
        if n_clicks > 0:
             return 'https://x.com/'  # Lien vers le réseau social
        return dash.no_update
    
    @app.callback(
    Output('url', 'href', allow_duplicate=True),
    Input('youtube-button', 'n_clicks'),
    prevent_initial_call=True
    )
    def go_to_yt(n_clicks):
        if n_clicks > 0:
             return 'https://www.youtube.com/@kutnitifoundation/featured'  # Lien vers le réseau social
        return dash.no_update
    
    @app.callback(
    Output('url', 'href', allow_duplicate=True),
    Input('linkedin-button', 'n_clicks'),
    prevent_initial_call=True
    )
    def go_to_linkedin(n_clicks):
        if n_clicks > 0:
             return 'https://www.linkedin.com/company/kutniti-foundation/'  # Lien vers le réseau social
        return dash.no_update
    
        
    @app.callback(
    Output('url', 'href', allow_duplicate=True),
    Input('insta-button', 'n_clicks'),
    prevent_initial_call=True
    )
    def go_to_insta(n_clicks):
        if n_clicks > 0:
             return 'https://www.instagram.com/kutniti/'  # Lien vers le réseau social
        return dash.no_update
    
    