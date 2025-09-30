import dash
import json
import pandas as pd
from dash.dependencies import Input, Output, State, ALL
from dash import callback_context
from app import app


# Abrir Modal Lawyers
@app.callback(
    Output('modal_processo', 'is_open'),
    Output('store_intermedio', 'data'),
    Input({'type':'editar_processo', 'index': ALL}, 'n_clicks'), # os botões de edição de todos os cards gerados
    Input('processo_button', 'n_clicks'), # o botão novo processo
    Input('cancel_button_novo_processo', 'n_clicks'), # o botão de cancelar do modal processo
    State('modal_processo', 'is_open'),
    State('store_proc', 'data'),
    State('store_intermedio', 'data'),
    prevent_initial_call=True
)
def open_modal_processo(n_editar,n_new, n_cancel, is_open, sotere_proc, store_intermedio):
    print('Callback abrir modal processos iniciado ==============')
    trigg_id = callback_context.triggered_id # já está implementado nesta versão de dash para obter o id do trigger!!!
                                               # alternativa seria: callbac_context.triggered[0]['prop_id'].split('.')[0]
    first_call = True if callback_context.triggered[0]['value'] == None else False

    if first_call:
        return is_open, store_intermedio
    
    if (trigg_id =='processo_button') or (trigg_id == 'cancel_button_novo_processo'):
        df_int = pd.DataFrame(store_intermedio)
        df_int = df_int[:-1]
        store_intermedio = df_int.to_dict()
        is_open = not is_open
        return is_open, store_intermedio
    
    if n_editar:
        trigg_dict = json.loads(callback_context.triggered[0]['prop_id'].split('.')[0])
        numero_processo = trigg_dict['index']
        df_int = pd.DataFrame(store_intermedio)
        df_proc = pd.DataFrame(sotere_proc)
        valores = df_proc.loc[df_proc['Nr Processo'] == numero_processo].values.tolist()
        valores = valores[0] + [True]
        df_int = df_int[:-1]
        df_int.loc[len(df_int)] = valores
        store_intermedio = df_int.to_dict()

        return not is_open, store_intermedio