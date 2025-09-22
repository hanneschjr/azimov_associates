
from dash import Input, Output, State
import pandas as pd

from app import app


@app.callback(
    Output('advogados_envolvidos', 'options'),
    Input('modal_processo', 'is_open'),
    State('store_adv', 'data'),
    prevent_initial_call=True
)
def update_dropdown_adv(is_open, store_dict):
    print('Callback_update_dropdown_adv_iniciado ============')
    if not store_dict:
        df_adv = pd.DataFrame(store_dict, columns=['Advogado', 'OAB', 'CPF'])
    else:
        df_adv = pd.DataFrame(store_dict) # converter para df facilita para criar a lista de advogados
    return [{'label': i, 'value': i} for i in df_adv['Advogado']]

