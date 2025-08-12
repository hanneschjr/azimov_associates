from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from app import app
from datetime import date
from db.queries import consulta_geral_advogados


# dados_adv = consulta_geral_advogados()
# df_adv = pd.DataFrame(dados_adv, columns=['Advogado', 'OAB', 'CPF'])

col_centered_style={'display': 'flex', 'justify-content': 'center'}


# ========= Layout ========= #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Adicionar um Processo")),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                # Empresa
                dbc.Label('Empresa', html_for='empresa_matriz'),
                dcc.Dropdown(id='empresa_matriz', clearable=False, className='dbc', options=['Escritório Matriz', 'Filial Porto Alegre', 'Filial Curitiba', 'Filial Canoas']),
                # Tipo de Processo
                dbc.Label('Tipo de Processo', html_for='tipo_processo'),
                dcc.Dropdown(id='tipo_processo', clearable=False, className='dbc', options=['Civil', 'Criminal', 'Previdenciário', 'Trabalhista', 'Vara de Família']),
                # Ação
                dbc.Label('Ação', html_for='acao'),
                dcc.Dropdown(id='acao', clearable=False, className='dbc', options=['Alimentos', 'Busca e Apreensão', 'Cautelar Inominada', 'Consignação', 'Habeas Corpus', 'Mandado de Segurança', 'Reclamação'])
            ], sm=12, md=4),
            dbc.Col([
                dbc.Label("Descrição", html_for='input_desc'),
                dbc.Textarea(id='input_desc', placeholder="Escreva aqui observações sobre o processo...",
                             style={'heigth': '80%'})
            ], sm=12, md=8)
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Label('Vara', html_for='vara'),
                dbc.RadioItems(id='vara',
                options=[{'label': 'Civil', 'Value': 'Civil'},
                {'label': 'Conciliação e Julgamento', 'value': 'Conciliação e Julgamento'},
                {'label': 'Trabalhista', 'value': 'Trabalhista'},
                {'label': 'Vara de Família', 'value': 'Vara de Família'}])
            ]),
            dbc.Col([
                dbc.Label('Fase', html_for='fase'),
                dbc.RadioItems(id='fase', inline=True,
                options=[{'label': 'Elaboração', 'Value': 'Elaboração'},
                {'label': 'Execução', 'value': 'Execução'},
                {'label': 'Impugnação', 'value': 'Impugnação'},
                {'label': 'Instrução', 'value': 'Instrução'},
                {'label': 'Recurso', 'value': 'Recurso'},
                {'label': 'Suspenso', 'value': 'Suspenso'}])
            ]),
            dbc.Col([
                dbc.Label('Instância', html_for='instancia'),
                dbc.RadioItems(id='instancia',
                options=[{'label': '1ª Instância', 'Value': 1},
                {'label': '2ª Instância', 'value': '2'},])
            ]),
        ]),
        html.Hr(),
        dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Data Inicial - Data Final")
                        ], style=col_centered_style),
                            dbc.Col([
                                dcc.DatePickerSingle(
                                    id='data_inicial',
                                    className='dbc',
                                    min_date_allowed=date(1999, 12, 31),
                                    max_date_allowed=date(2030, 12, 31),
                                    initial_visible_month=date.today(),
                                    date=date.today()
                                ),
                                dcc.DatePickerSingle(
                                    id='data_final',
                                    className='dbc',
                                    min_date_allowed=date(1999, 12, 31),
                                    max_date_allowed=date(2030, 12, 31),
                                    initial_visible_month=date.today(),
                                    date=None
                                ),
                            ], style=col_centered_style),
                        ]),
                    html.Br(),
                    dbc.Switch(id='processo_concluido', label='Processo Concluido', value=False),
                    dbc.Switch(id='processo_vencido', label='Processo Vencido', value=False),
                    html.P("O filtro de data final só será computado se o checklist estiver marcado.", className="dbc", style={'font-size': '80%'}),
                ], sm=12, md=5),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Selecione o advogado responsável"),
                            dcc.Dropdown(
                                id='advogados_envolvidos',
                                className='dbc'
                            )
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Input(id="input_cliente", placeholder="Nome completo do cliente...", type="text")
                        ])
                    ], style={'margin-top': '15px', 'padding': '15px'}),
                    dbc.Row([
                        dbc.Col([
                        dbc.Input(id='input_cliente_cpf', placeholder='CPF do cliente (apenas números)...', type='number')
                        ])
                    ], style={'padding': '15px'}),
                ], sm=12, md=7),
                html.Hr(),
                ])


    ])
], id='modal_processo', size='lg', is_open=True)