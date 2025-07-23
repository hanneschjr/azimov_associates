from dash import html
import dash_bootstrap_components as dbc
from app import app


# =========== Layout ========= #

layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Cadastro de Advogados')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                html.H5(id='div_erro2')
            ])
        ])
    ]),
    dbc.ModalFooter([
        dbc.Button('Sair', id='modal_adv_quit_button', color='danger'),
    ])
], id='modal_adv_confirm', size='sm', is_open=False)
