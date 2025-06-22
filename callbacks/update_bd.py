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



# Dcc.Store back to file
@app.callback(
    Output('div_fantasma', 'children'), 
    Input('store_adv', 'data'),
    Input('store_proc', 'data'),
)
def update_file(adv_data, proc_data):
    if not adv_data:
        return []

    df_adv_aux = pd.DataFrame(adv_data)
    df_proc_aux = pd.DataFrame(proc_data) if proc_data else pd.DataFrame()

    for _, row in df_adv_aux.iterrows():
        add_adv(row['Advogado'], row['OAB'], row['CPF'])

    return []
