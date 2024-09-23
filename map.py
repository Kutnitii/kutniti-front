import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

color_scale = ['#CD1313', '#E1A014', '#5BCB15'] 
data = [["USA", "Canada", "Brazil", "Germany", "Russia", "France"], [1, 2, 4, 5, 6, 0]]


df = pd.DataFrame({
    'Country': data[0],
    'Positivity': data[1],
    'Info': ["United States Info", "Canada Info", "Brazil Info", "Germany Info", "Russia Info", "France Info"]
})


app = dash.Dash(__name__)

fig = px.choropleth(df,
                    locations='Country',
                    locationmode="country names",  
                    color="Positivity", 
                    projection="equirectangular",
                    color_continuous_scale=color_scale
                   )

fig.update_geos(showcoastlines=True, coastlinecolor="Black",
                showland=True, landcolor="#C7C7C7",
                showocean=True, oceancolor="#26232C",
                showcountries=True, countrycolor="black",
                showlakes=True, lakecolor="#26232C",
                center=dict(lat=25, lon=75),
                projection_scale=1.5 
                )

fig.update_layout(coloraxis_showscale=False,
                  margin=dict(l=0, r=0, t=0, b=0))

app.layout = html.Div([
    dcc.Graph(figure=fig, id='world-map',config={'displayModeBar':False})  # Display the world map
],  className="map_holder")


@app.callback(
    Output('world-map', 'figure'),
    Input('world-map', 'clickData')
)
def log_clicked_country(clickData):
    if clickData:
        country = clickData['points'][0]['location']
        print(f"Clicked country: {country}")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)