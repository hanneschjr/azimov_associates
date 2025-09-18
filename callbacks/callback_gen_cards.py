from dash import html, Input, Output, State
import dash_bootstrap_components as dbc

# import from folders
from app import * 


@app.callback(
    Output('card_generator', 'children'), # é um container dentro de home
    Output('advogados_filter', 'value'), # é o dropdown dentro de home
    Output('procesos_filter', 'value'),
    Output('input_cpf_pesquisa', 'value'),
    Input('pesquisar_cpf', 'n_clicks'),
    Input('todos_processos', 'n_clicks'),
    Input('advogados_filter', 'value'),
    Input('pesquisar_num_proc', 'n_clicks'),
    Input('store_proc', 'data'),
    Input('store_adv', 'data'),
    Input('switches_input', 'value'),
    Input('checklist_input', 'value'),
    State('processos_filter', 'value'),
    State('input_cpf_pesquisa', 'value')
)
def 