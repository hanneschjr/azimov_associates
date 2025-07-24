import dash
from dash import Input, Output, State, callback_context
import pandas as pd


from app import app

@app.callback(
    Output('store_adv', 'data'),
    Output('div_erro2', 'children'),
    Output('div_erro2', 'style'),
    Output('adv_nome', 'value'),
    Output('adv_oab', 'value'),
    Output('adv_cpf', 'value'),
    Output('modal_new_lawyer', 'is_open'),
    Input('save_button_novo_advogado', 'n_clicks'),
    Input('cancel_button_novo_advogado', 'n_clicks'),
    Input('new_adv_button', 'n_clicks'),
    State('store_adv', 'data'),
    State('adv_nome', 'value'),
    State('adv_oab', 'value'),
    State('adv_cpf', 'value'),
    State('modal_new_lawyer', 'is_open')
)
def add_new_adv(n_save, n_cancel, n_open, dataset, nome, oab, cpf, is_open):
    ctx = callback_context

    # protege de acionamentos inesperados na inicialização e do app e contra quebras
    if not ctx.triggered:
        return dataset, [], {}, nome, oab, cpf, is_open
    # Detecta qual botão foi clicado
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Se clicou em "Cancelar"
    if trigger_id == 'cancel_button_novo_advogado':
        return dataset, [], {}, '', '', '', False

    # Se clicou em "Novo Advogado" para abrir o modal
    if trigger_id == 'new_adv_button':
        return dataset, [], {}, nome, oab, cpf, True

    # Se clicou em "Salvar"
    if trigger_id == 'save_button_novo_advogado':
        if None in [nome, oab, cpf]:
            return dataset, ['Todos os dados são obrigatórios para registro!'], \
                   {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}, \
                   nome, oab, cpf, True


        if df_adv.empty or not all(col in df_adv.columns for col in ['Advogado', 'OAB', 'CPF']):
            df_adv = pd.DataFrame(columns=['Advogado', 'OAB', 'CPF']) # dataframe vazio com as colunas

        # print(dataset)

        if str(oab) in df_adv['OAB'].values:
            return dataset, ['Número de OAB já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True
        
        elif str(cpf) in df_adv['CPF'].values:
            return dataset, ['Número de CPF já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True
        
        elif nome in df_adv['Advogado'].values:
            return dataset, [f'Nome {nome} já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True

        # df_adv.loc[df_adv.shape[0]] = [nome, oab, cpf]
        # dataset = df_adv.to_dict('records')

        # return dataset, ['Cadastro realizado com sucesso!'], \
        #        {'margin-bottom': '15px', 'color': 'green'}, '', '', '', True

    # Fallback padrão
    return dataset, [], {}, nome, oab, cpf, is_open