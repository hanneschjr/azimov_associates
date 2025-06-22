import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

# init database
from db import init_db
init_db()

# import from folders
from app import * 
from components import home, sidebar
from db.connect import *
import pandas as pd
from db.queries import consulta_geral_advogados, consulta_geral_processos, add_adv


# ====================== Callbacks =================== #
# URL callback to update page content
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def render_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
    else:
        return dbc.Container([
            html.H1('404: Not found', className='text-danger'),
            html.Hr(),
            html.P(f"O caminho '{pathname}' não foi reconhecido..."),
            html.P('Use a NavBar para retornar ao sistema de maneira correta.')
        ])
