from dash import html, dcc
import dash_bootstrap_components as dbc

def create_main_layout():
    return html.Div(
        [
        dcc.Location(id='url', refresh=True),
        dbc.Container([
            dcc.Link(html.Img(src="/assets/Kutniti_watch_logo.svg"), href="/", className="kutniti_logo"),
            html.Nav([
                dcc.Link("Countries", href="/countries", className='nav-link'),
                dcc.Link("Newspapers", href="/newspapers", className='nav-link'),
                dcc.Link("Latest Articles", href="/articles", className='nav-link'),
                dcc.Link("Methodology", href="/methodology", className='nav-link'),
                dcc.Link("About", href="/about", className='nav-link')
                ], className="navigation"),
            html.Nav([
                html.Button(html.Img(src='/assets/youtube-logo.png', style={"height":"3vh","width":"3vh"}), id='youtube-button', n_clicks=0, className="social_button"),
                html.Button(html.Img(src="/assets/X-logo.png", style={"height":"3vh","width":"3vh"}), id='twitter-button', n_clicks=0, className="social_button"),
                html.Button(html.Img(src='/assets/linkedin-logo.png', style={"height":"3vh","width":"3vh"}), id='linkedin-button', n_clicks=0, className="social_button"),
                html.Button(html.Img(src='/assets/insta-logo.png', style={"height":"3vh","width":"3vh"}), id='insta-button', n_clicks=0, className="social_button"),
                ], className="socials"),
            ], className="header"),
        html.Div(id='page-content'),
        ])

def home_layout():
    return html.Div([
        html.H2("Bienvenue sur Mon Site Interactif"),
        html.P("Explorez notre carte interactive pour découvrir des informations fascinantes sur les pays du monde.")
    ])

def about_layout():
    return html.Div([
        html.H2("À propos"),
        html.P("Ce site a été créé pour fournir des informations interactives sur les pays du monde.")
    ])
