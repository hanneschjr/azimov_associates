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
        df_int = df_int[-1:]
        store_intermedio = df_int.to_dict()
        return not is_open, store_intermedio
    
    if n_editar:
        trigg_dict = json.loads(callback_context.triggered[0]['prop_id'].split('.')[0])
        numero_processo = trigg_dict['index']
        df_int = pd.DataFrame(store_intermedio)
        # print(f'dataframe int: {df_int}, colunas int: {df_int.columns}')
        df_proc = pd.DataFrame(sotere_proc)
        # print(f'dataframe proc: {df_proc}, colunas: {df_proc.columns}')
        valores = df_proc.loc[df_proc['Nr Processo'] == str(numero_processo)].values.tolist()
        valores = valores[0] + [True] # lista com o valor True no final
        # print(f'valores: {valores}')
        df_int = df_int[-1:]
        df_int.loc[len(df_int)] = valores
        # print(f'dataframe int depois: {df_int}')
        store_intermedio = df_int.to_dict()
        print(f'store_intermedio: {store_intermedio}')
        return not is_open, store_intermedio