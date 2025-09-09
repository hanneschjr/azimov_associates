import dash
from dash import Input, Output, State, callback_context
import pandas as pd
from utils.inputs_validates import validar_cpf, validar_oab
from db.queries import consulta_geral_advogados

from app import app
from app import cache

@app.callback(
    Output('store_adv', 'data'),
    Output('div_erro2', 'children'),
    Output('div_erro2', 'style'),
    Output('adv_nome', 'value'),
    Output('adv_oab', 'value'),
    Output('adv_cpf', 'value'),
    Output('modal_new_lawyer', 'is_open'),
    Output('temporizador', 'disabled'),
    Input('save_button_novo_advogado', 'n_clicks'),
    Input('cancel_button_novo_advogado', 'n_clicks'),
    Input('new_adv_button', 'n_clicks'),
    Input('temporizador', 'n_intervals'),
    State('store_adv', 'data'),
    State('adv_nome', 'value'),
    State('adv_oab', 'value'),
    State('adv_cpf', 'value'),
    State('modal_new_lawyer', 'is_open'),
    prevent_initial_call=False
)
def atualizar_store_limpar_campos_formulario(n_save, n_cancel, n_open, n_intervals, dataset, nome, oab, cpf, is_open):
    ctx = callback_context

    # protege de acionamentos inesperados na inicialização e do app e contra quebras
    if not ctx.triggered:
        print("Iniciando o store_adv")
        dados_adv = consulta_geral_advogados()
        dataset = pd.DataFrame(dados_adv, columns=['id','Advogado', 'OAB', 'CPF'])
        dataset.drop("id", axis=1, inplace=True)
        dataset = dataset.to_dict('records').copy()

        return dataset, [], {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    
    # Detecta qual botão foi clicado
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # se o temporizador estiver acionando o n_intervals
    if trigger_id == 'temporizador':
        return dash.no_update, [], {}, '', '', '', dash.no_update, True

    # Se clicou em "Cancelar"
    if trigger_id == 'cancel_button_novo_advogado':
        return dash.no_update, [], {}, '', '', '', False, dash.no_update

    # Se clicou em "Novo Advogado" para abrir o modal
    if trigger_id == 'new_adv_button':
        return dash.no_update, [], {}, dash.no_update, dash.no_update, dash.no_update, True, dash.no_update

    # Se clicou em "Salvar" em "Adicionar Novo Advogado"
    if trigger_id == 'save_button_novo_advogado':
        if None in [nome, oab, cpf]:
            print(f'{nome}, {oab}, {cpf}')
            return dash.no_update, ['Todos os dados são obrigatórios para registro!'], \
                   {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}, \
                   nome, oab, cpf, True, dash.no_update
  
        df_adv = pd.DataFrame(dataset)

        # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
        # print(df_adv)
        # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')
        if df_adv.empty or not all(col in df_adv.columns for col in ['Advogado', 'OAB', 'CPF']):
            df_adv = pd.DataFrame(columns=['Advogado', 'OAB', 'CPF']) # cria um dataframe vazio com as colunas

        # print(df_adv)
        # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')

        if str(oab) in df_adv['OAB'].values:
            return dash.no_update, ['Número de OAB já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False
        
        elif str(cpf) in df_adv['CPF'].values:
            return dash.no_update, ['Número de CPF já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False
        
        elif not validar_cpf(cpf):
            return dash.no_update, ['Número de CPF inválido!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False

        elif not validar_oab(oab):
            return dash.no_update, ['Número OAB inválido!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False
        
        elif nome in df_adv['Advogado'].values:
            return dash.no_update, [f'Nome {nome} já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False

        df_adv.loc[df_adv.shape[0]] = [nome, oab, cpf]
        dataset = df_adv.to_dict('records')
        print("Callback Adicionar Advogado Acionado! =======")
        print(f'{dataset}')

        return dataset, ['Cadastro realizado com sucesso!'], \
               {'margin-bottom': '15px', 'color': 'green'}, '', '', '', True, False


    # Fallback padrão
    return dash.no_update, [], {}, nome, oab, cpf, is_open, dash.no_update

