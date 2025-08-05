from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

# ============= Layout ============== #
layout = dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle('Adicione Um Advogado')),
    dbc.ModalBody([
        dbc.Row([
            dbc.Col([
                dbc.Label("OAB"),
                dbc.Input(id="adv_oab", placeholder="Apenas números, referente a OAB ...",
                          type="text", 
                          inputMode="numeric",   # ativa teclado numérico em celulares
                          pattern=r"\d*",        # sugere apenas dígitos
                          maxLength=20,
                          valid=None)

            ], sm=12, md=6),
            dbc.Col([
                dbc.Label("CPF"),
                dbc.Input(id="adv_cpf", placeholder="Apenas número, referente ao CPF ...",
                          type="text", 
                          inputMode="numeric",   # ativa teclado numérico em celulares
                          pattern=r"\d*",        # sugere apenas dígitos
                          maxLength=11,
                          valid=None)
            ], sm=12, md=6), 
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Label('Nome'),
                dbc.Input(id='adv_nome', placeholder='Nome completo do advogado...', type='text')
                
            ]),
        ]),
        html.H5(['Essa é a nossa div de ERRO'], id='div_erro2'),
        dcc.Interval(id='temporizador', interval=5*1000, n_intervals=0, disabled=True)
    ]),
    dbc.ModalFooter([
        dbc.Button("Cancelar", id="cancel_button_novo_advogado", color="danger", n_clicks=0),
        dbc.Button("Salvar", id="save_button_novo_advogado", color="success", n_clicks=0),
    ])
], id="modal_new_lawyer", size='lg', is_open=False)

# valid = "False"
# # =========== Callbacks ========= #
# @app.callback(
#     Output('store_adv', 'data'),
#     Output('div_erro2', 'cildren'),
#     Output('div_erro2', 'style'),
#     Input('save_button_novo_advogado', 'n_clics'),
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
#             return dataset, ['Todos dados são obrigatórios para registro!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        
#         df_adv = pd.DataFrame(dataset)

#         if oab in df_adv['OAB'].values:
#             return dataset, ['Número de OAB já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
#         elif cpf in df_adv['CPF'].values:
#             return dataset, ['Número de CPF já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
#         elif nome in df_adv['Advogado'].values:
#             return dataset, [f'Nome {nome} já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}
        
#         df_adv.loc[df_adv.shape[0]] = [nome, oab, cpf]
#         dataset = df_adv.to_dict()

#         return dataset, ['Cadastro realizado com sucesso!'], {'margin-bottom': '15px', 'color': 'green', 'text-shadow': '2px 2px 8px #000000'}
#     return dataset, erro, style