from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from config import Config
import plotly.express as px
from dash import html

def register_callbacks(app):
    df = pd.read_csv(Config.DATA_PATH)

    @app.callback(
        [Output('carte-monde', 'figure'), Output('details-pays', 'children')],
        [Input('carte-monde', 'clickData')]
    )
    def update_map(click_data):
        fig = go.Figure(data=go.Choropleth(
            locations=df['code_pays'],
            z=df['valeur'],
            text=df['nom_pays'],
            colorscale='Viridis',
            autocolorscale=False,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_title='Valeur'
        ))

        fig.update_layout(
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='equirectangular',
                bgcolor='rgba(0,0,0,0)',
                lakecolor='#000000',
                landcolor='#1a1a1a',
                subunitcolor='#272727',
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin={"r":0,"t":0,"l":0,"b":0}
        )

        details = html.Div("Click on a country to see some details.")

        if click_data:
            pays_clique = click_data['points'][0]['location']
            donnees_pays = df[df['code_pays'] == pays_clique].iloc[0]
            details = html.Div([
                html.H3(donnees_pays['nom_pays']),
                html.P(f"Population: {donnees_pays['population']:,}"),
                html.P(f"PIB: ${donnees_pays['pib']:,}"),
            ])

        return fig, details

    @app.callback(
        [Output('additional-graph', 'figure'), 
        Output('additional-graph', 'style')],
        [Input('carte-monde', 'clickData')]
    )
    def update_additional_graph(click_data):
        if click_data:
            pays_clique = click_data['points'][0]['location']
            donnees_pays = df[df['code_pays'] == pays_clique]

            fig = px.bar(
                donnees_pays,
                x='nom_pays',
                y='population',
                title='Population par pays',
                color_discrete_sequence=['#636efa'],
            )

            fig.update_layout(
                title_font=dict(color='white'),
                xaxis=dict(
                    title='Pays',
                    color='white',
                    showgrid=False,
                    linecolor='darkgray',
                ),
                yaxis=dict(
                    title='Population',
                    color='white',
                    showgrid=False,
                    linecolor='darkgray',
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin={"r":0,"t":50,"l":0,"b":0},
                transition = {
                    'duration': 500,
                    'easing': 'cubic-in-out'
                }
            )

            fig.update_traces(marker_line_color='darkgray', marker_line_width=1.5)

            return fig, {'display': 'block'}

        return go.Figure(), {'display': 'none'}


    @app.callback(
        [Output('sentiment-bar', 'figure'), 
        Output('sentiment-bar', 'style')],
        [Input('carte-monde', 'clickData')]
    )
    def update_sentiment_bar(click_data):
        if not click_data:
            return go.Figure(), {'display': 'none'}

        pays_clique = click_data['points'][0]['location']
        donnees_pays = df[df['code_pays'] == pays_clique].iloc[0]

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=[donnees_pays['positive']],
            y=['Sentiment'],
            orientation='h',
            marker=dict(
                color='rgba(50, 205, 50, 0.8)',
                line=dict(color='rgba(0, 0, 0, 1)', width=2)
            ),
            name='Positive',
            text=[f"{donnees_pays['positive']}%"],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(color='black')
        ))

        fig.add_trace(go.Bar(
            x=[donnees_pays['neutral']],
            y=['Sentiment'],
            orientation='h',
            marker=dict(
                color='rgba(255, 214, 10, 0.8)',
                line=dict(color='rgba(0, 0, 0, 1)', width=2)
            ),
            name='Neutral',
            text=[f"{donnees_pays['neutral']}%"],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(color='black'),
        ))

        fig.add_trace(go.Bar(
            x=[donnees_pays['negative']],
            y=['Sentiment'],
            orientation='h',
            marker=dict(
                color='rgba(255, 69, 58, 0.8)',  # Rouge pour négatif
                line=dict(color='rgba(0, 0, 0, 1)', width=2)
            ),
            name='Negative',
            text=[f"{donnees_pays['negative']}%"],  # Texte dans la barre
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(color='black'),
        ))

        fig.update_layout(
            barmode='stack',
            xaxis=dict(
                title='',
                showgrid=False,
                zeroline=False,
                visible=False
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                visible=False
            ),
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=100,
            dragmode=False
        )
        
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)

        return fig, {'display': 'block'}