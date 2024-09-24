from dash import html, dcc

def create_main_layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Header([
            html.H1("Mon Site Interactif")
        ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#222', 'color': 'white'}),
        html.Nav([
            dcc.Link("Accueil", href="/", className='nav-link'),
            dcc.Link("Carte Interactive", href="/carte", className='nav-link'),
            dcc.Link("À propos", href="/about", className='nav-link')
        ], style={'display': 'flex', 'justifyContent': 'center', 'padding': '10px', 'backgroundColor': '#333'}),
        html.Div(id='page-content', style={'padding': '20px'}),
        html.Footer([
            html.P("© 2024 Mon Site Interactif")
        ], style={'textAlign': 'center', 'padding': '10px', 'backgroundColor': '#222', 'color': 'white'})
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
