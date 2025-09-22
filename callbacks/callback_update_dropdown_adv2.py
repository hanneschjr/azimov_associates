from dash import Input, Output, State
import pandas as pd
from dash import callback_context

from app import app


@app.callback(
    Output('advogados_filter', 'options'),
    Input('store_adv', 'data'),
    prevent_initial_call=True
)
def update_dropdown_adv_two(store_dict):
    print('Callback_update_dropdown_adv_2 iniciado ============')

    if not store_dict:
        df_adv = pd.DataFrame(store_dict, columns=['Advogado', 'OAB', 'CPF'])
        # df_adv.drop('id', axis=1, inplace=True)
    else:
        df_adv = pd.DataFrame(store_dict) # converter para df facilita para criar a lista de advogados

    return [{'label': i, 'value': i} for i in df_adv['Advogado']]
