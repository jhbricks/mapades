import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from deff.mapa import mapa

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.RadioItems(
            id='area-selector',
            options=[
                {'label': 'Paraná', 'value': 'Parana'},
                {'label': 'Núcleo Territorial Central de Curitiba', 'value': 'NTC_Curitiba'}
            ],
            value='Parana',
            labelStyle={'display': 'block'}
        )
    ], style={'margin-bottom': '20px'}),
    
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='category-selector-1',
                options=[
                    {'label': 'Contextualização', 'value': 'Contextualizacao'},
                    {'label': 'Renda', 'value': 'Renda'},
                    {'label': 'Riqueza', 'value': 'Riqueza'}
                ],
                placeholder="Selecione uma categoria..."
            ),
            dcc.Dropdown(
                id='indicator-selector-1',
                placeholder="Selecione um indicador..."
            ),
            html.Button('Submit', id='submit-button-1')
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='category-selector-2',
                options=[
                    {'label': 'Contextualização', 'value': 'Contextualizacao'},
                    {'label': 'Renda', 'value': 'Renda'},
                    {'label': 'Riqueza', 'value': 'Riqueza'}
                ],
                placeholder="Selecione uma categoria..."
            ),
            dcc.Dropdown(
                id='indicator-selector-2',
                placeholder="Selecione um indicador..."
            ),
            html.Button('Submit', id='submit-button-2')
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ], style={'margin-bottom': '20px'}),

    html.Div([
        dcc.Graph(id='map-1'),
        dcc.Graph(id='map-2')
    ])
])

# Callback to update indicator dropdown options based on selected category
@app.callback(
    Output('indicator-selector-1', 'options'),
    Output('indicator-selector-2', 'options'),
    Input('category-selector-1', 'value'),
    prevent_initial_call=True
)
def update_indicator_options(category):
    # Add logic to provide indicator options based on selected category
    # You may need to replace this with your specific logic
    if category == 'Contextualizacao':
        indicators = ['Populacao', 'Densidade demografica', 'Grau de urbanizacao']
    elif category == 'Renda':
        indicators = ['Indice Gini', 'Renda media da populacao', 'Renda da populacao feminina']
    else:
        indicators = ['Domicilios com bens duraveis', 'Numero de veiculos por pessoas', 'Populacao declarante do IRPF']

    options = [{'label': indicator, 'value': indicator} for indicator in indicators]

    return options, options

# Callback to update the map based on selected area, category, and indicator
@app.callback(
    Output('map-1', 'figure'),
    Output('map-2', 'figure'),
    Input('area-selector', 'value'),
    Input('category-selector-1', 'value'),
    Input('indicator-selector-1', 'value'),
    Input('submit-button-1', 'n_clicks'),
    Input('category-selector-2', 'value'),
    Input('indicator-selector-2', 'value'),
    Input('submit-button-2', 'n_clicks'),
)
def update_maps(area, cat1, ind1, n_clicks1, cat2, ind2, n_clicks2):
    # Add logic to generate maps based on selected area, category, and indicator
    # You may need to replace this with your specific logic
    if n_clicks1 is not None and ind1 == 'Populacao':
        figure1 = mapa(area, contexto, 'Populacao', 'FisherJenks', 5, 'copper_r', ['Municipio', 'Populacao'], 'Populacao (hab)')
    else:
        figure1 = {}  # Provide a default empty figure or handle other cases

    if n_clicks2 is not None and ind2 == 'Indice Gini':
        figure2 = mapa(area, renda, 'Indice Gini', 'FisherJenks', 3, 'PuBuGn', ['Municipio', 'Indice Gini'], 'Indice Gini')
    else:
        figure2 = {}  # Provide a default empty figure or handle other cases

    return figure1, figure2


if __name__ == '__main__':
    app.run_server(debug=True)
