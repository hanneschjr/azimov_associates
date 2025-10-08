# Arquivo app do Software de Gestão de Escritório de Advocacia - Pjt Azimov modificado
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
import os
import pandas as pd
from db import init_db
# onde pega os ícones e o tema LUX
# baixa os bootstrap templates que tem ligação com o LUX (só o css)
# a folha de estilos é o front-awesome + dbc.theme + css
estilos = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css', dbc.themes.LUX] 
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css" 

app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css]) 

# suprime o lançamentos de exceções que alguns callbacks podem conter
# informa oa Dash que ele deve servir seus arquivos JavaScript internamente, a partir do próprio servidor Flask (localmente)
# app é o app Desh, app.server é o app Flask interno e server = app.server torna disponível fora do Dash
app.config['suppress_callback_exceptions'] = True 
app.scripts.config.serve_locally = True 
server = app.server 


# import from folders

from components import home, sidebar
from db.connect import *

# init database
if __name__ == '__main__':
    init_db()




# Importações dos callbacks =====================================
import callbacks.callaback_update_store_adv
import callbacks.callaback_update_store_proc
import callbacks.callback_render_page
import callbacks.callback_render_table_adv
import callbacks.callback_toggle_modal
import callbacks.callback_update_dropdown_adv
import callbacks.callback_open_modal_processos
import callbacks.callback_gen_cards



# Criar estrutura para Store intermediária ===============
data_int = {
    'Nr Processo':{},
    'Empresa':{},
    'Tipo':{}, 
    'Ação':{}, 
    'Vara':{}, 
    'Fase':{},
    'Instância':{}, 
    'Data Inicial':{}, 
    'Data Final':{}, 
    'Processo Concluído':{},
    'Processo Vencido':{}, 
    'Advogado':{}, 
    'Cliente':{}, 
    'CPF Cliente':{}, 
    'Descrição':{},
    'disabled':{}
}

# ====================== Layout =================== #
app.layout = dbc.Container([
    # Store e Location
    dcc.Location(id='url'),
    dcc.Store(id='store_intermedio', data=data_int),
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




