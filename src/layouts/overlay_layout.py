from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd
from utils.data_processing import data_world_sunbrust;

color_scale = [ '#5BCB15','#E1A014','#CD1313'] 

def create_overlayout(name_country="World"):
    filtered_df = data_world_sunbrust.loc[data_world_sunbrust['name'] == name_country]

    if filtered_df.empty:
        return html.Div([
            html.P(f"No data available for {name_country}")
        ], className="overlay")

   
    positive_value = int(filtered_df['positive'].values[0])
    neutral_value = int(filtered_df['neutral'].values[0])
    negative_value = int(filtered_df['negative'].values[0])

    
    labels = ['Positive', 'Neutral', 'Negative']
    values = [positive_value, neutral_value, negative_value]

    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  
        textinfo='label+value',
        insidetextfont=dict(color='white'),
        outsidetextfont=dict(color='white'),
         marker=dict(
            colors=color_scale,
            line=dict(
                color='black',  
                width=2  )))])
    
    
    fig.update(layout_showlegend=False)
    fig.update_traces(insidetextorientation='horizontal', marker=dict(line=dict(width=0)))

   
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(255, 255, 255, 0)', 
        plot_bgcolor='rgba(255, 255, 255, 0)', 
        autosize=True,
        uirevision='constant',
        annotations=[dict(text=name_country, x=0.5, y=0.5,
                      font_size=40, font_color='#FFFFFF',showarrow=False, xanchor="center")],
        font=dict(
        size=20,
        weight='bold'
    )
        
    )

    return html.Div([
        html.Div(f"Perception of India in {name_country}",id="Title_graph", className="text_info"),
        dcc.Graph(
            id='pie_chart', 
            figure=fig, 
            config={'staticPlot': True, 'displayModeBar': False}, 
            className="sunburst"
        ),
        html.Div(f"Number of Articles: {data_world_sunbrust['nbr_articles'].values[0]}", className="text_info"),
        html.Div("More Details",id="More_info", className="more_info"),
        html.Div(id='log-output'),
    ], className="overlay")