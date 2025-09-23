import dash
from dash import Input, Output, State, callback_context
import pandas as pd
from datetime import date
from utils.inputs_validates import validar_cpf, validar_oab
from db.queries import consulta_geral_processos

from app import app
@app.callback(
    Output('store_proc', 'data'), #1
    Output('div_erro', 'children'), #2
    Output('div_erro', 'style'), #3
    Output('empresa_matriz', 'value'), #4
    Output('tipo_processo', 'value'),#5
    Output('acao', 'value'), #6
    Output('input_desc', 'value'), #7
    Output('vara', 'value'), #8
    Output('fase', 'value'), #9
    Output('instancia', 'value'), #10
    Output('data_inicial', 'date'), #11
    Output('data_final', 'date'), #12
    Output('processo_concluido', 'value'), #13
    Output('processo_vencido', 'value'), #14
    Output('advogado_envolvido', 'value'), #15
    Output('input_cliente', 'value'), #16
    Output('input_cliente_cpf', 'value'), #17
    Output('input_no_processo', 'value'), #18
    Output('modal_processo', 'is_open'), #19 controle do modal
    Output('temporizador2', 'disabled'), #20 desabilita o temporizador
    Input('save_button_novo_processo', 'n_clicks'), #1
    Input('cancel_button_novo_processo', 'n_clicks'), #2 limpeza e controle do modal
    Input('processo_button', 'n_clicks'),  #3 controle do modal
    Input('temporizador2', 'n_intervals'), #4 
    State('store_proc', 'data'), #5
    State('empresa_matriz', 'value'), #6 controle do modal
    State('tipo_processo', 'value'), #6 controle do modal
    State('acao', 'value'), #6 controle do modal
    State('advogado_envolvido', 'value'), #6 controle do modal
    State('input_cliente', 'value'), #6 controle do modal
    State('input_cliente_cpf', 'value'), #6 controle do modal
    State('input_no_processo', 'value'), #6 controle do modal
    prevent_initial_call=False
)
def atualizar_store_limpar_campos_form_proc(n_save, n_cancel, n_processo, n_intervals, dataset, empresa, tipo, acao, adv, cliente, cliente_cpf, nr_processo):
    ctx = callback_context
    
    # protege de acionamentos inesperados na inicialização e do app e contra quebras
    if not ctx.triggered:
        print("Iniciando o store_proc ==========")
        print(f'{empresa}, {tipo}, {acao}, {adv}, {cliente}, {cliente_cpf}, {nr_processo}')
        dados_proc = consulta_geral_processos()
        dataset = pd.DataFrame(dados_proc, columns=['id','Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase',
                                                     'Instância', 'Data Inicial', 'Data Final', 'Processo Concluído',
                                                     'Processo Vencido', 'Advogado', 'Cliente', 'CPF Cliente', 'Descrição'])
        dataset.drop("id", axis=1, inplace=True)
        dataset = dataset.to_dict('records').copy()
        return dataset, [], {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

        # return dash.no_update, [], {}, None, None, None, None, "Civil", \
        #     'Elaboração', 1, date.today(), None, False, False, \
        #     None, None, None, None, True

    # Detecta qual botão foi clicado
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Se o temporizador for acionando -> apaga a Div e desabilita o próprio temporizador
    if trigger_id == 'temporizador2':
        return dataset, [], {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, True


    # Se clicou em "Cancelar" -> fecha o modal e limpa todos os campos
    if trigger_id == 'cancel_button_novo_processo':
        return dash.no_update, [], {}, None, None, None, None, None, \
            None, None, date.today(), None, False, False, \
            None, None, None, None, False, dash.no_update
    
    # Se clicou no botão "Processos" na Sidebar:
    if trigger_id == 'processo_button':
                return dash.no_update, [], {}, None, None, None, None, None, \
            None, None, date.today(), None, False, False, \
            None, None, None, None, True, dash.no_update


    # Se clicou em "Salvar" em "Adicionar Novo Processo"
    if trigger_id == 'save_button_novo_processo':
        if None in [empresa, tipo, acao, adv, cliente, cliente_cpf, nr_processo]:
            print(f'{empresa}, {tipo}, {acao}, {adv}, {cliente}, {cliente_cpf}, {nr_processo}')
            return dash.no_update, ['Por favor, preencha todos os campos obrigatórios para registro!'], \
                   {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}, \
                   dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
                   dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
                   dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, False
  
        # df_adv = pd.DataFrame(dataset)

        # # Previne se o df estiver vazio e sem colunas
        # if df_adv.empty or not all(col in df_adv.columns for col in ['Advogado', 'OAB', 'CPF']):
        #     df_adv = pd.DataFrame(columns=['Advogado', 'OAB', 'CPF']) # cria um dataframe vazio com as colunas

        # # print(df_adv)
        # # print('xxxxxxxxxxxxxxxxxxxxxxxxxx')

        # if str(oab) in df_adv['OAB'].values:
        #     return dash.no_update, ['Número de OAB já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False
        
        # elif str(cpf) in df_adv['CPF'].values:
        #     return dash.no_update, ['Número de CPF já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False
        
        # elif not validar_cpf(cpf):
        #     return dash.no_update, ['Número de CPF inválido!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False

        # elif not validar_oab(oab):
        #     return dash.no_update, ['Número OAB inválido!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False
        
        # elif nome in df_adv['Advogado'].values:
        #     return dash.no_update, [f'Nome {nome} já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, nome, oab, cpf, True, False

        # df_adv.loc[df_adv.shape[0]] = [nome, oab, cpf]
        # dataset = df_adv.to_dict('records')
        # print("Callback Adicionar Advogado Acionado! =======")
        # print(f'{dataset}')

        # return dataset, ['Cadastro realizado com sucesso!'], \
        #        {'margin-bottom': '15px', 'color': 'green'}, '', '', '', True, False


    # Fallback padrão
    # return dash.no_update, [], {}, nome, oab, cpf, is_open, dash.no_update

