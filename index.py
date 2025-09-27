import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd


# init database
from db import init_db

if __name__ == '__main__':
    init_db()

# import from folders
from app import *
from components import home, sidebar
from db.connect import *
from db.queries import consulta_geral_advogados, consulta_geral_processos


# import callbacks
import callbacks.callaback_update_store_adv
import callbacks.callback_render_page
import callbacks.callback_render_table_adv
import callbacks.callback_toggle_modal
import callbacks.callback_update_db
import callbacks.callback_update_dropdown_adv
# import callbacks.callback_open_modal_processos
import callbacks.callback_update_dropdown_adv2
import callbacks.callaback_update_store_proc


# Criar estrutura para Store intermediária ===============




# ====================== Layout =================== #
app.layout = dbc.Container([
    # Store e Location
    dcc.Location(id='url'),
    dcc.Store(id='store_intermedio'),
    dcc.Store(id='store_adv'),
    dcc.Store(id='store_proc'),
    html.Div(id='div_fantasma'),

    # Layout
    dbc.Row([
        dbc.Col([
            sidebar.layout
        ], md=2, style={'padding': '0px'}),
        dbc.Col([
            dbc.Container(id='page-content', fluid=True, style={'height': '100%', 'width': '100%', 'padding-left': '14px', 'backgroundColor': "#C9C5C5" })
        ], md=10, style={'padding': '0px'})

    ])

], fluid=True)

# ====================== Callbacks =================== #


if __name__ == '__main__':
    app.run(debug=True, port=8050, host='0.0.0.0', use_reloader=True)
    






