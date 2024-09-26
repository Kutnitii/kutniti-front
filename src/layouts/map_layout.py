from dash import html, dcc
from dash import html, dcc
import plotly.express as px
from utils.data_processing import df;
import dash_bootstrap_components as dbc

#def create_map_layout():
#    return html.Div([
#        html.Div(id="sidebar", className="sidebar", children=[
#            html.H3("Country information"),
#            html.Div(id='details-pays', children=[
#                html.P("Click on a country to see some details.")
#            ]),
#            dcc.Graph(id='additional-graph', config={'displayModeBar': False}, style={'display': 'none'}),
#            html.P("Click on a country to see some details."),
#            dcc.Graph(id='sentiment-bar', config={'displayModeBar': False, 'staticPlot': True}, style={'display': 'none'}),
#            html.P("Click on a country to see some details.")
#        ]),
#        dcc.Graph(id='carte-monde', config={'displayModeBar': False}),
#    ], className='map-container')

color_scale = [[0, '#5BCB15'],[0.5,'#E1A014'],[1,'#CD1313']] 
fig = px.choropleth(df,
                    locations='nom_pays',
                    locationmode="country names",  
                    color="valeur", 
                    projection="equirectangular",
                    color_continuous_scale=color_scale,
                    range_color=[0,100],
                   )

fig.update_geos(showcoastlines=True, coastlinecolor="Black",
                showland=True, landcolor="#C7C7C7",
                showocean=True, oceancolor="#26232C",
                showcountries=True, countrycolor="black",
                showlakes=True, lakecolor="#26232C",
                projection_rotation=dict(lon=0, lat=0),
                projection_scale=1.2,
                framecolor="#26232C")

fig.update_layout(coloraxis_showscale=False,
                  margin=dict(l=0, r=0, t=0, b=0),
                  paper_bgcolor='rgba(255,0,0,0)',
                    plot_bgcolor='rgba(0,255,0,0)',
                  dragmode='zoom',
                  autosize=True,
                  uirevision='constant'               
                  )

def create_map_layout():
    return dbc.Container([
        dbc.Container(
            dbc.Container(
                dcc.Graph(id='world-map', config={
                    'displayModeBar': False,
                }),
                className="map"),
            className="map-container"),
        html.Div(className="bottom_darkening"),
        html.Div(className="right_darkening"),
        html.Div(className="left_darkening")
    ])

