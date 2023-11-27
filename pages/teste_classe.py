import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import geopandas as gpd
from deff.mapa import mapa
from deff.mapa import grafico
from deff.calculos import conta

# Create Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H3("Contextualização - Mapa da Desigualdade"),
    
    # Select area
    html.H3("Contextualização"),
    dcc.RadioItems(
        id='area-selector',
        options=[
            {'label': 'Paraná', 'value': 'PR'},
            {'label': 'Núcleo Territorial Central de Curitiba', 'value': 'NTCC'},
        ],
        value='PR',
        labelStyle={'display': 'block'}
    ),

    # Select indicator
    dcc.RadioItems(
        id='indicator-selector',
        options=[
            {'label': 'Localização', 'value': 'Location'},
            {'label': 'População residente', 'value': 'Population'},
            {'label': 'Densidade demográfica', 'value': 'Density'},
            {'label': 'Grau de urbanização', 'value': 'Urbanization'},
            {'label': 'População feminina', 'value': 'FemalePopulation'},
            {'label': 'População preta/parda', 'value': 'BlackBrownPopulation'},
            {'label': 'Razão de dependência', 'value': 'DependencyRatio'},
        ],
        value='Population',
        labelStyle={'display': 'block'}
    ),

    # Display Map and Graph
    html.Div(id='map-container'),
    html.Div(id='graph-container'),

    # Additional Information
    html.Div([
        html.P("Ano-base: 2021"),
        html.P("Fonte(s): IBGE"),
        html.P("Fórmula: População total por município"),
        html.P("Observações: Prévia da população por município do Censo Demográfico 2022 do IBGE.")
    ]),
])

# Callbacks to update map and graph based on user selections
@app.callback(
    [Output('map-container', 'children'),
     Output('graph-container', 'children')],
    [Input('area-selector', 'value'),
     Input('indicator-selector', 'value')]
)
def update_content(selected_area, selected_indicator):
    map_figure = None
    graph_figure = None

    if selected_area == 'PR':
        if selected_indicator == 'Population':
            map_figure = mapa('PR', contexto, 'População', 'FisherJenks', 5, 'copper_r', ['Município', 'População'], 'População (hab)')
            graph_figure = conta('PR', contexto, 'População', 2021, 'População total', 'soma', 'habitantes')
            graph_figure = grafico('PR', contexto, 'População', 'Habitantes')

        # Add more conditions for other indicators...

    return map_figure, graph_figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
