from dash import html
import dash_bootstrap_components as dbc

def gerar_card_padrao(qtd_proc):
    card_padrao = dbc.Card([
        dbc.CardBody([
            html.H3(f"{qtd_proc} PROCESSOS ENCONTRADOS", style={'font-weight': 'bold', 'color': 'white'})
        ])
    ], style={'height': '100%', 'margin-bottom': '12px', 'background-color': '#646464'})
    return card_padrao