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
import callbacks.callaback_update_store_proc
import callbacks.callback_render_page
import callbacks.callback_render_table_adv
import callbacks.callback_toggle_modal
import callbacks.callback_update_db
import callbacks.callback_update_dropdown_adv
import callbacks.callback_open_modal_processos
import callbacks.callback_update_dropdown_adv2
import callbacks.callback_gen_cards



# Criar estrutura para Store intermediária ===============
data_int = {
    'Nr Processo':[],
    'Empresa':[],
    'Tipo':[], 
    'Ação':[], 
    'Vara':[], 
    'Fase':[],
    'Instância':[], 
    'Data Inicial':[], 
    'Data Final':[], 
    'Processo Concluído':[],
    'Processo Vencido':[], 
    'Advogado':[], 
    'Cliente':[], 
    'CPF Cliente':[], 
    'Descrição':[],
    'disabled':[]
}

df_int = pd.DataFrame(data_int)

# ====================== Layout =================== #
app.layout = dbc.Container([
    # Store e Location
    dcc.Location(id='url'),
    dcc.Store(id='store_intermedio', data=df_int.to_dict()),
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
    app.run(debug=False, port=8050, host='0.0.0.0', use_reloader=False)
    






