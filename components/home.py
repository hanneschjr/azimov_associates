import dash_bootstrap_components as dbc
from dash import html, dcc
from app import app
import pandas as pd

from db.queries import consulta_geral_advogados


# ========== Styles =========== #
card_style = {'height': '100%', 'margin-bottom': '12px'}


# =========== Layout ========== #
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3("ENCONTRE O PROCESSO QUE VOCÊ PROCURA", style={'text-align': 'left', 'margin-left': '32px'})
        ], className='text-center')
    ], style={'margin-top': '14px'}),
    html.Hr(style={"border": "1px solid black"}),
    dbc.Row([
        # Coluna dos Filtros
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.H3("Nº DO PROCESSO")
                                ], sm=12)
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id='processos_filter', placeholder="Insira...", type="number")
                                ], sm=12, md=12, lg=8),
                                dbc.Col([
                                    dbc.Button([html.I(className='fa fa-search')], id="pesquisar_num_proc", color='dark')
                                ], sm=12, md=12, lg=4)
                            ], style={'margin-bottom': '32px'}),
                            dbc.Row([
                                dbc.Col([
                                    html.H3("STATUS")
                                ])
                            ], style={'margin-top': '32px'}),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Checklist(
                                        options=[{"label": "Concluídos", "value": 1}, {"label": "Vencidos", "value": 2}],
                                        value=[],
                                        id="switches_input",
                                        switch=True,
                                    ),
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.H3("INSTÂNCIA")
                                ])
                            ], style={'margin-top': '24px'}),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Checklist(
                                        options=[{"label": "1a Instância", "value": 1}, 
                                                {"label": "2a Instância", "value": 2}],
                                        value=[1, 2],
                                        id="checklist_input"
                                    ),
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.H3("CPF DO CLIENTE")
                                ])
                            ], style={'margin-top': '24px'}),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button([html.I(className='fa fa-search')], id="pesquisar_cpf", color='light')
                                ], sm=2),
                                dbc.Col([
                                    dbc.Input(id="input_cpf_pesquisa", placeholder="DIGITE O CPF", type="number")
                                ], sm=10)
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.H3("ADVOGADO")
                                ])
                            ], style={'margin-top': '24px'}),
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(
                                        id='advogados_filter',
                                        placeholder='SELECIONE O ADVOGADO',
                                        className='dbc'
                                    ),
                                ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button("Todos os Processos", id="todos_processos", style={'width': '100%'}, color="dark")
                                ])
                            ], style={'margin-top': '24px'})
                        ], style={'margin': '20px'})
                    ])
                ])
            ])
        ], sm=12, md=5, lg=4),
        # Coluna dos cards
        dbc.Col([
            dbc.Container(id='card_generator', fluid=True, style={'width': '100%', 'padding': '0px 0px 0px 0px', 'margin': '0px 0px 0px 0px'}),
            html.Div(id='div_fant')
        ], sm=12, md=7, lg=8, style={'padding-left': '0px'})
    ])

], fluid=True, style={'height': '100%', 'padding': '10px', 'margin': 0, 'padding-left': 0, })