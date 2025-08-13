import dash
from dash.dependencies import Input, Output
import pandas as pd
from dash import dash_table, callback_context
from dash.dash_table.Format import Group
from app import app
from components import home
from db.queries import consulta_geral_advogados

@app.callback(
    Output('advogados_envolvidos', 'options'),
    Input('store_adv', 'data')
)
def fill_drop_adv(data):
    ctx = callback_context

    # protege de acionamentos inesperados na inicialização e do app e contra quebras
    if not ctx.triggered:
        if data:
            dados_adv = consulta_geral_advogados()
            df_adv = pd.DataFrame(dados_adv, columns=['Advogado', 'OAB', 'CPF'])
            adv_list = list(df_adv['Advogado'])
            return adv_list
        return []

    # Detecta qual botão foi clicado
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print( f'{trigger_id}, {data}')

    # Este fluxo é menos oneroso pois não vai ao banco
    if data:
        df = pd.DataFrame(data)
        adv_list = list(df['Advogado'])
        return adv_list
    return []