import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd


from app import app


# ============= Layout ============== #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicione Um Advogado')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Label("OAB"),
                dbc.Input(id="adv_oab", placeholder="Apenas números, referente a OAB ...", type="number")
            ], sm=12, md=6),
            dbc.Col([
                dbc.Label("CPF"),
                dbc.Input(id="adv_cpf", placeholder="Apenas número, CPF...", type='number')
            ], sm=12, md=6), 
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Label('Nome'),
                dbc.Input(id='adv_nome', placeholder='Nome completo do advogado...', type='text')
            ]),
        ]),
        html.H5(id='div_erro2')
    ]),
    dbc.ModalFooter([
        dbc.Button("Cancelar", id="cancel_button_novo_advogado", color="danger", n_clicks=0),
        dbc.Button("Salvar", id="save_button_novo_advogado", color="success", n_clicks=0),
    ])
], id="modal_new_lawyer", size='lg', is_open=False)


# =========== Callbacks ========= #
# @app.callback(
#     Output('store_adv', 'data'),
#     Output('div_erro2', 'children'),
#     Output('div_erro2', 'style'),
#     Output('adv_nome', 'value'),
#     Output('adv_oab', 'value'),
#     Output('adv_cpf', 'value'),
#     Output('modal_new_lawyer', 'is_open'),
#     Input('save_button_novo_advogado', 'n_clicks'),
#     State('store_adv', 'data'),
#     State('adv_nome', 'value'),
#     State('adv_oab', 'value'),
#     State('adv_cpf', 'value')
# )
# def novo_adv(n, dataset, nome, oab, cpf):
#     erro = []
#     style = {}
#     if n:
#         if None in [nome, oab, cpf]:
#             return dataset, ['Todos dados são obrigatórios para registro!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}, True
        
#         df_adv = pd.DataFrame(dataset)
#         if df_adv.empty or not all(col in df_adv.columns for col in ['Advogado', 'OAB', 'CPF']):
#             # Inicializa com colunas vazias (mas nomeadas)
#             df_adv = pd.DataFrame(columns=['Advogado', 'OAB', 'CPF'])



#         if oab in df_adv['OAB'].values:
#             return dataset, ['Número de OAB já exixte no sistema!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}, nome, oab, cpf, True
#         elif cpf in df_adv['CPF'].values:
#             return dataset, ['Número de CPF já exixte no sistema!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}, nome, oab, cpf, True
#         elif nome in df_adv['Advogado'].values:
#             return dataset, [f'Nome {nome} já exixte no sistema!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}, nome, oab, cpf, True
        
#         df_adv.loc[df_adv.shape[0]] = [nome, oab, cpf]
#         dataset = df_adv.to_dict('records')

#         return dataset, ['Cadastro realizado com sucesso!'], {'margin-bottom': '15px', 'color': 'green', 'text-shadow': '2px 2px 8px #000000'}, False
#     return dataset, erro, style, nome, oab, cpf, True



