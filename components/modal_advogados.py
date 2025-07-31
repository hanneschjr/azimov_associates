from dash import html
import dash_bootstrap_components as dbc
from app import app


# =========== Layout ========= #

layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Cadastro de Advogados')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                html.Div(id='table_adv', className='dbc')
            ])
        ])
    ]),
    dbc.ModalFooter([
        dbc.Button('Sair', id='quit_button', color='danger'),
        dbc.Button('Novo', id='new_adv_button', color='success')
    ])
], id='modal_lawyers', size='lg', is_open=False
)
