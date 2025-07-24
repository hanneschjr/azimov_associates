from dash import html
import dash_bootstrap_components as dbc
from app import app


# ============= Layout ============== #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicione Um Advogado')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Label("OAB"),
                dbc.Input(id="adv_oab", placeholder="Apenas números, referente a OAB ...", type="number")
            ], sm=12, md=6),
            dbc.Col([
                dbc.Label("CPF"),
                dbc.Input(id="adv_cpf", placeholder="Apenas número, CPF...", type='number')
            ], sm=12, md=6), 
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Label('Nome'),
                dbc.Input(id='adv_nome', placeholder='Nome completo do advogado...', type='text')
            ]),
        ]),
        html.H5(['Essa é a nossa div de ERRO'], id='div_erro2')
    ]),
    dbc.ModalFooter([
        dbc.Button("Cancelar", id="cancel_button_novo_advogado", color="danger", n_clicks=0),
        dbc.Button("Salvar", id="save_button_novo_advogado", color="success", n_clicks=0),
    ])
], id="modal_new_lawyer", size='lg', is_open=False)

