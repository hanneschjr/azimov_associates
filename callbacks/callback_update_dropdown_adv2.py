from dash import Input, Output, State
import pandas as pd
from dash import callback_context

from app import app


@app.callback(
    Output('advogados_filter', 'options'),
    Input('store_adv', 'data'),
    Input('deletar_processo', 'n_clicks'),
    Input('editar_processo', 'n_clicks'),
    Input('cancel_button_novo_processo', 'n_clicks'),
    prevent_initial_call=True
)
def update_dropdown_adv_two(store_dict, n_clicks):
    print('Callback_update_dropdown_adv_2 iniciado ============')

    if not store_dict:
        # df_adv = pd.DataFrame(store_dict, columns=['Advogado', 'OAB', 'CPF'])
        return []

    df_adv = pd.DataFrame(store_dict) # converter para df facilita para criar a lista de advogados
    options = [{'label': i, 'value': i} for i in df_adv['Advogado']]
    return options
    

    
