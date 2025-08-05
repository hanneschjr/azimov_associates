from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app


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
        ])


    ])
], id='modal_processo', size='lg', is_open=True)