import dash
from dash import Input, Output, State, callback_context
import pandas as pd
from utils.inputs_validates import validar_cpf, validar_oab
from db.queries import consulta_geral_processos

from app import app
@app.callback(
    Output('store_proc', 'data'),
    Output('div_erro', 'children'),
    Output('div_erro', 'style'),
    Output('empresa_matriz', 'value'),
    Output('tipo_processo', 'value'),
    Output('acao', 'value'),
    Output('input_desc', 'value'),
    Output('vara', 'value'),
    Output('fase', 'value'),
    Output('instancia', 'value'),
    Output('data_inicial', 'date'),
    Output('data_final', 'date'),
    Output('processo_concluido', 'value'),
    Output('processo_vencido', 'value'),
    Output('advogado_envolvido', 'value'),
    Output('input_cliente', 'value'),
    Output('input_cliente_cpf', 'value'),
    Output('input_no_processo', 'value'),
    Output('modal_processo', 'is_open'),
    Input('save_button_novo_processo', 'n_clicks'),
    Input('cancel_button_novo_processo', 'n_clicks'),
    Input('temporizador2', 'n_intervals'),
    State('store_proc', 'data'),
    State('modal_processo', 'is_open'),
    prevent_initial_call=False
)
def atualizar_store_proc_limpar_campos_formulario(n_save, n_cancel, n_intervals, dataset, is_open):
    ctx = callback_context
    
    # protege de acionamentos inesperados na inicialização e do app e contra quebras
    if not ctx.triggered:
        print("Iniciando o store_proc ==========")
        dados_proc = consulta_geral_processos()
        dataset = pd.DataFrame(dados_proc, columns=['id','Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase',
                                                     'Instância', 'Data Inicial', 'Data Final', 'Processo Concluído',
                                                     'Processo Vencido', 'Advogado', 'Cliente', 'CPF Cliente', 'Descrição'])
        dataset.drop("id", axis=1, inplace=True)
        dataset = dataset.to_dict('records').copy()
        return dataset, [], {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    
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

        # Previne se o df estiver vazio e sem colunas
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

