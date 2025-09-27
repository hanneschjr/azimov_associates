from dash import Input, Output
import pandas as pd
from time import sleep

# import from folders
from app import * 
from db.queries import add_adv, add_proc



# Dcc.Store back to file
@app.callback(
    Output('div_fantasma', 'children'),
    Input('store_adv', 'data'),
    Input('store_proc', 'data'),
    prevent_initial_call=True
)
def update_db_adv(adv_data, proc_data):
    if not adv_data:
        response = []
    else:
        row_adv = adv_data[-1]
        add_adv(row_adv['Advogado'], row_adv['OAB'], row_adv['CPF'])
        response = []

    if not proc_data:
        response = []
    else:
        row_proc = proc_data[-1]
        add_proc(row_proc['Nr Processo'], row_proc['Empresa'], row_proc['Tipo'],
                row_proc['Ação'], row_proc['Vara'], row_proc['Fase'],
                row_proc['Instância'], row_proc['Data Inicial'], row_proc['Data Final'],
                row_proc['Processo Concluído'], row_proc['Processo Vencido'], row_proc['Advogado'],
                row_proc['Cliente'], row_proc['CPF Cliente'], row_proc['Descrição'],)
        response = []
    print('Callback de insersão do item na base de dados acioando! =========')
    sleep(5)

    return response
