from dash import html, dcc
import plotly.express as px
from utils.data_processing import df;
import dash_bootstrap_components as dbc
import pandas as pd


def create_figure(min_threshold, max_threshold):
    df_filtered = df.copy()
    df_filtered['sentiment'] = df_filtered['sentiment'].apply(lambda x: x if (x <= (max_threshold/100) and x >= (min_threshold/100)) else None)
    df_filtered = df_filtered.dropna(subset=['sentiment'])
    
    
    if len(df_filtered) == 0:
        color_scale = [[0, '#C7C7C7'], [1, '#C7C7C7']]  # Gray color scale
        fig = px.choropleth(df,
                    locations='name',
                    locationmode="country names",  
                    color="sentiment", 
                    projection="equirectangular",
                    color_continuous_scale=color_scale,
                    range_color=[0,100],
                    height=900, width=1800
                   )

        fig.update_geos(showcoastlines=True, coastlinecolor="Black",
                showland=True, landcolor="#C7C7C7",
                showocean=True, oceancolor="#26232C",
                showcountries=True, countrycolor="black",
                showlakes=True, lakecolor="#26232C",
                projection_rotation=dict(lon=0, lat=0),
                projection_scale=1.5,
                framecolor="#26232C")

        fig.update_layout(coloraxis_showscale=False,
                  margin=dict(l=0, r=0, t=0, b=0),
                  paper_bgcolor='rgba(255,0,0,0)',
                  plot_bgcolor='rgba(0,255,0,0)',
                  dragmode='zoom',
                  autosize=True,
                  uirevision='constant'               
                  )
        return fig
    
    
    color_scale = [[0,'#CD1313' ],[0.5,'#E1A014'],[1,'#5BCB15']] 
    fig = px.choropleth(df_filtered,
                    locations='name',
                    locationmode="country names",  
                    color="sentiment", 
                    projection="equirectangular",
                    color_continuous_scale=color_scale,
                    range_color=[0,1],
                    height=900, width=1800
                   )

    fig.update_geos(showcoastlines=True, coastlinecolor="Black",
                showland=True, landcolor="#C7C7C7",
                showocean=True, oceancolor="#26232C",
                showcountries=True, countrycolor="black",
                showlakes=True, lakecolor="#26232C",
                projection_rotation=dict(lon=0, lat=0),
                projection_scale=1.5,
                framecolor="#26232C")

    fig.update_layout(coloraxis_showscale=False,
                  margin=dict(l=0, r=0, t=0, b=0),
                  paper_bgcolor='rgba(255,0,0,0)',
                  plot_bgcolor='rgba(0,255,0,0)',
                  dragmode='zoom',
                  autosize=True,
                  uirevision='constant'       
                  )
    return fig



def create_map_layout():
    return dbc.Container([
        dbc.Container(
            dbc.Container(
                dcc.Graph(id='world-map', figure=create_figure(0,100),config={
                    'displayModeBar': False,
                    }),
                className="map"),
            className="map-container"),
        
        html.Div(className="bottom_darkening"),
        html.Div(className="right_darkening"),
        html.Div(className="left_darkening"),
        
        html.Div([
            dcc.RangeSlider(id='my-slider',min=0,max=100,step=1,value=[0,100],marks={i: f"{i}%" for i in [100, 0]},allowCross=False,included=True,tooltip={"placement": "bottom", "always_visible": True},className="slider"),
            html.Button(className="calendar"),
            dcc.Input(className="search_bar", placeholder="Search for keywords"),
        ], className="tool_bar")
    ])

