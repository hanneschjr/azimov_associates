import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd


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
        html.H5( id='dif_erro2')
    ]),
    dbc.ModalFooter([
        dbc.Button("Cancelar", id="cancel_button_novo_advogado", color="danger"),
        dbc.Button("Salvar", id="save_button_novo_advogado", color="success"),
    ])
], id="modal_new_lawyer", size='lg', is_open=False)


# =========== Callbacks ========= #
@app.callback(
    Output('store_adv', 'data'),
    Output('div_erro2', 'cildren'),
    Output('div_erro2', 'style'),
    Input('save_button_novo_advogado', 'n_clics'),
    State('store_adv', 'data'),
    State('adv_nome', 'value'),
    State('adv_oab', 'value'),
    State('adv_cpf', 'value')
)
def novo_adv(n, dataset, nome, oab, cpf):
    erro = []
    style = {}

    if n:
        if None in [nome, oab, cpf]:
            return dataset, ['Todos dados são obrigatórios para registro!'], 