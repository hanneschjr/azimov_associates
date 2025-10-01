import dash
from dash import Input, Output, State, callback_context, ALL
import pandas as pd
from datetime import date
from utils.inputs_validates import validar_cpf, validar_oab
from db.queries import consulta_geral_processos

from app import app
@app.callback(
    Output('store_proc', 'data'), #1
    Output('div_erro', 'children'), #2
    Output('div_erro', 'style'), #3
    Output('input_no_processo', 'value'), #4
    Output('empresa_matriz', 'value'), #5
    Output('tipo_processo', 'value'),#6
    Output('acao', 'value'), #7
    Output('vara', 'value'), #8
    Output('fase', 'value'), #9
    Output('instancia', 'value'), #10
    Output('data_inicial', 'date'), #11
    Output('data_final', 'date'), #12
    Output('processo_concluido', 'value'), #13
    Output('processo_vencido', 'value'), #14
    Output('advogados_envolvidos', 'value'), #15
    Output('input_cliente', 'value'), #16
    Output('input_cliente_cpf', 'value'), #17
    Output('input_desc', 'value'), #18
    Output('input_no_processo', 'disable'), #19
    Output('temporizador2', 'disabled'), #20 desabilita o temporizador

    Input('processo_button', 'n_clicks'),  #1
    Input('save_button_novo_processo', 'n_clicks'), #2
    Input({'type': 'deletar_processo', 'index': ALL}, 'n_clicks'), #3
    Input('store_intermedio', 'data'), #4
    Input('temporizador2', 'n_intervals'), #5

    State('modal_processo', 'is_open'), #6
    State('store_proc', 'data'), #7
    State('input_no_processo', 'value'), #8 
    State('empresa_matriz', 'value'), #9 
    State('tipo_processo', 'value'), #10 
    State('acao', 'value'), #11 
    State('vara', 'value'), #12 
    State('fase', 'value'), #13 
    State('instancia', 'value'), #14 
    State('data_inicial', 'date'), #15 
    State('data_final', 'date'), #16 
    State('processo_concluido', 'value'), #17 
    State('processo_vencido', 'value'), #18 
    State('advogados_envolvidos', 'value'), #19  
    State('input_cliente', 'value'), #20 
    State('input_cliente_cpf', 'value'), #21 
    State('input_desc', 'value'), #22 
    prevent_initial_call=False
)
def crud_form_proc(n_new_proc, n_save, n_delete, store_int, n_interval, is_open, store_proc, no_processo,
                                            empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin,
                                            concl, venc, adv, cliente, cliente_cpf,  descricao):
    ctx = callback_context
    


    # protege de acionamentos inesperados na inicialização e do app e contra quebras
    # first_call = True if (ctx.triggered[0]['value'] == None or ctx.triggered[0]['value'] == False) else False
    trigg_id = ctx.triggered_id

    if not ctx.triggered:
        print("Iniciando o store_proc ==========")
        dados_proc = consulta_geral_processos()
        df_proc = pd.DataFrame(dados_proc, columns=['id','Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase',
                                                     'Instância', 'Data Inicial', 'Data Final', 'Processo Concluído',
                                                     'Processo Vencido', 'Advogado', 'Cliente', 'CPF Cliente', 'Descrição'])
        df_proc.drop("id", axis=1, inplace=True)
        store_proc = df_proc.to_dict('records').copy()
        no_processo = empresa = tipo = acao = vara = fase = instancia = data_ini = data_fin = adv = cliente = cliente_cpf = descricao = None
        concl = venc = False
        return store_proc, [], {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, False, True

    if trigg_id == 'save_button_novo_processo':
        df_proc = pd.DataFrame(store_proc, columns=['Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase',
                                                     'Instância', 'Data Inicial', 'Data Final', 'Processo Concluído',
                                                     'Processo Vencido', 'Advogado', 'Cliente', 'CPF Cliente', 'Descrição'])
    
        df_int = pd.DataFrame(store_int, columns=['Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase',
                                                     'Instância', 'Data Inicial', 'Data Final', 'Processo Concluído',
                                                     'Processo Vencido', 'Advogado', 'Cliente', 'CPF Cliente', 'Descrição', 'disabled'])

        if len(df_int.index) == 0:
            if None in [no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, adv, cliente, cliente_cpf]:
                return store_proc, ['Todos dados são obrigatórios para registro!'], {'margin-bottom': '15px', 'color': 'red'}, \
                no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, concl, venc, adv, cliente, cliente_cpf, descricao, False, False

            if (no_processo in df_proc['Nr Processo'].values):
                return store_proc, ['Número de processo já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, no_processo,  \
                 empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, concl, venc, adv, cliente, cliente_cpf, descricao, False, False

            data_ini = pd.to_datetime(data_ini).date()
            try:
                data_fin = pd.to_datetime(data_fin).date()
            except:
                pass

            df_proc.reset_index(drop=True, inplace=True)

            concl = 0 if concl == False else 1
            venc = 0 if venc == False else 1

            if concl == 0: data_fin = None

            df_proc.loc[df_proc.shape[0]] = [no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin,
                                             concl, venc, adv, cliente, cliente_cpf, descricao]

            store_proc = df_proc.to_dict('records')
            no_processo = empresa = tipo = acao = vara = fase = instancia = data_ini = data_fin = adv = cliente = cliente_cpf = descricao = None
            concl = venc = False

            return store_proc, ['Processo salvo com sucesso!'], {'margin-bottom': '15px', 'color': 'green'}, \
                no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, \
                concl, venc, adv, cliente, cliente_cpf, descricao, False, False
        else:
            pass


    # # Detecta qual botão foi clicado
    # trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # # Se o temporizador for acionando -> apaga a Div e desabilita o próprio temporizador
    # if trigger_id == 'temporizador2':
    #     return dataset, [], {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
    #         dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
    #         dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, True

    # # Se clicou em "Cancelar" -> fecha o modal e limpa todos os campos
    # if trigger_id == 'cancel_button_novo_processo':
    #     return dash.no_update, [], {}, None, None, None, None, None, \
    #         None, None, date.today(), None, False, False, \
    #         None, None, None, None, False, dash.no_update
    
    # # Se clicou no botão "Processos" na Sidebar:
    # if trigger_id == 'processo_button':
    #             return dash.no_update, [], {}, None, None, None, None, None, \
    #         None, None, date.today(), None, False, False, \
    #         None, None, None, None, True, dash.no_update

    # # Se clicou em "Salvar" em "Adicionar Novo Processo"
    # if trigger_id == 'save_button_novo_processo':
    #     if None in [empresa, tipo, acao, vara, fase, instancia, adv, cliente, cliente_cpf, nr_processo]:
    #         # print(f'{empresa}, {tipo}, {acao}, {adv}, {cliente}, {cliente_cpf}, {nr_processo}')
    #         return dash.no_update, ['Por favor, preencha todos os campos obrigatórios para registro!'], \
    #                {'margin-bottom': '15px', 'color': 'red', 'text-shadow': '2px 2px 8px #000000'}, \
    #                dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
    #                dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
    #                dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, False
        
    #     df_proc = pd.DataFrame(dataset)
    #     colunas_proc = ['Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase', 'Instância', 'Data Inicial',
    #                     'Data Final', 'Processo Concluído','Processo Vencido', 'Advogado', 'Cliente',
    #                     'CPF Cliente', 'Descrição']
        
    #     # Previne se o df estiver vazio e sem colunas
    #     if df_proc.empty or not all(col in df_proc.columns for col in colunas_proc):
    #         df_proc = pd.DataFrame(columns=colunas_proc) # cria um dataframe vazio com as colunas

    #     # testa se o nr do processo já está cadastrado
    #     if str(nr_processo) in df_proc['Nr Processo'].values:
    #         return dash.no_update, ['Número do processo já existe no sistema!'], {'margin-bottom': '15px', 'color': 'red'}, \
    #                dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
    #                dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
    #                dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, False

    #     # feito todos os teste, insere o registro na última posição para ser gravado no store:
    #     df_proc.loc[df_proc.shape[0]] = [nr_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin,
    #                                         concl, venc, adv, cliente, cliente_cpf, descricao]
    #     dataset = df_proc.to_dict('records')
    #     print("Callback Atualizar Store Proc Acionado! =======")
    #     return dataset, ['Cadastro realizado com sucesso!'], {'margin-bottom': '15px', 'color': 'green'}, \
    #          None, None, None, None, None, None, None, date.today(), None, False, False, None, None, None, \
    #          None, False, False
        # return store_proc, [], {}, no_processo, empresa, tipo, acao, vara, fase, \
        #     instancia, data_ini, data_fin, concl, venc, adv, cliente, cliente_cpf, \
        #     descricao, False, True
    # Fallback padrão
    return dash.no_update, [], {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

