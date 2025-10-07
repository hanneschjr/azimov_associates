import dash
from dash import callback_context, Input, Output, State, ALL
import pandas as pd
from datetime import date
from utils.inputs_validates import validar_cpf, validar_oab
from db.queries import consulta_geral_processos, add_proc, update_proc, delete_proc
import json

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
    Output('input_no_processo', 'disabled'), #19
    Output('temporizador2', 'disabled'), #20 desabilita o temporizador


    # Input('processo_button', 'n_clicks'),  #1
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
def crud_form_proc(n_save, n_delete, store_int, n_intervals, is_open, store_proc, no_processo,
                                            empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin,
                                            concl, venc, adv, cliente, cliente_cpf,  descricao):
    triggered = callback_context.triggered
    trigg_id = callback_context.triggered_id
    


    # protege de acionamentos inesperados na inicialização e do app e contra quebras
    # first_call = True if (ctx.triggered[0]['value'] == None or ctx.triggered[0]['value'] == False) else False


    if not trigg_id:
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
    
    if trigg_id == 'temporizador2':
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

        # Criação processo
        if len(df_int.index) == 0: 
            if None in [no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, adv, cliente, cliente_cpf]:
                return store_proc, ['Todos dados são obrigatórios para registro!'], {'margin-bottom': '15px', 'color': 'red'}, \
                no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, concl, venc, adv, cliente, cliente_cpf, descricao, False, False

            if (str(no_processo) in df_proc['Nr Processo'].values):
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
            
            
            add_proc(no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, concl, venc, adv, cliente, cliente_cpf, descricao)
            print('Inseridos no processo com sucesso! =========')

            store_proc = df_proc.to_dict('records')
            no_processo = empresa = tipo = acao = vara = fase = instancia = data_ini = data_fin = adv = cliente = cliente_cpf = descricao = None
            concl = venc = False
            return store_proc, ['Processo salvo com sucesso!'], {'margin-bottom': '15px', 'color': 'green'}, \
                no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, \
                concl, venc, adv, cliente, cliente_cpf, descricao, False, False 
        
        # Edição de processo
        else:
            concl = 0 if concl == False else 1
            venc = 0 if venc == False else 1
            if concl == 0: data_fin = None

            # Editar processo na base de dados:
            update_proc(no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, concl, venc, adv, cliente, cliente_cpf, descricao)
            print(f'Processo nº {no_processo} atualizado com sucesso! =========')

            # Edita processo no dicionário store_proc:
            index = df_proc.loc[df_proc['Nr Processo'] == str(no_processo)].index[0]
            df_proc.loc[index, df_proc.columns] = [no_processo, empresa, tipo, acao, vara, fase, instancia, 
                                                   data_ini, data_fin, concl, venc, adv, cliente, cliente_cpf,
                                                   descricao]
            store_proc = df_proc.to_dict('records')
            no_processo = empresa = tipo = acao = vara = fase = instancia = data_ini = data_fin = adv = cliente = cliente_cpf = descricao = None
            concl = venc = False
            
            return store_proc, ['Processo salvo com sucesso!'], {'margin-bottom': '15px', 'color': 'green'}, \
                no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, \
                concl, venc, adv, cliente, cliente_cpf, descricao, False, False 
        
    # preencher os campos do formulário
    if (trigg_id == 'store_intermedio') and is_open:
        try:
            df_int = pd.DataFrame(callback_context.triggered[0]['value'])
            df_proc = pd.DataFrame(store_proc, columns=['Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase',
                                                     'Instância', 'Data Inicial', 'Data Final', 'Processo Concluído',
                                                     'Processo Vencido', 'Advogado', 'Cliente', 'CPF Cliente', 'Descrição'])
            # df_proc.drop("id", axis=1, inplace=True)
            valores = df_int.head(1).values.tolist()[0] 
            no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, concl, venc, adv, cliente, cliente_cpf,  descricao, disable = valores
            concl = False if concl == 0 else True
            venc = False if venc == 0 else True   
            return dash.no_update, ['Modo de Edição: Número de processo não pode ser alterado!'], {'margin-bottom': '15px', 'color': 'green'}, \
                no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, \
                concl, venc, adv, cliente, cliente_cpf, descricao, disable, False
        
        except:
            no_processo = empresa = tipo = acao = vara = fase = instancia = data_ini = data_fin = concl = venc = adv = cliente = cliente_cpf =  descricao = None
            concl = venc = False
            return store_proc, [], {}, \
                no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, \
                concl, venc, adv, cliente, cliente_cpf, descricao, False, True
        
    # deletar processo
    # if str(no_processo) in n_delete:
    if triggered:
        raw_id = triggered[0]['prop_id'].split('.')[0]
        try:
            trigg_id_dict = json.loads(callback_context.triggered[0]['prop_id'].split('.')[0])
            trigg_type = trigg_id_dict.get('type', None)
        except:
            trigg_type = raw_id
        if trigg_type:   
            df_proc = pd.DataFrame(store_proc, columns=['Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase',
                                                        'Instância', 'Data Inicial', 'Data Final', 'Processo Concluído',
                                                        'Processo Vencido', 'Advogado', 'Cliente', 'CPF Cliente', 'Descrição'])
            # trigg_id_dict = json.loads(callback_context.triggered[0]['prop_id'].split('.')[0])
            numero_processo = trigg_id_dict['index']

            # apaga da base de dados o registro
            registro_deletado = delete_proc(str(numero_processo))
            if registro_deletado:
                print(f'O Processo Nr {registro_deletado[1]} foi apagado com sucesso! ================')
            else:
                print('Nenhum registro foi encontrado para apagar. ==============')

            # apaga o registro do dataframe
            index_processo = df_proc.loc[df_proc['Nr Processo'] == str(numero_processo)].index[0]
            df_proc.drop(index_processo, inplace=True)
            df_proc.reset_index(drop=True, inplace=True)
            # retorna o dataframe em dict
            store_proc = df_proc.to_dict()
            no_processo = empresa = tipo = acao = vara = fase = instancia = data_ini = data_fin = concl = venc = adv = cliente = cliente_cpf =  descricao = None
            concl = venc = False

            return store_proc, [], {}, \
                    no_processo, empresa, tipo, acao, vara, fase, instancia, data_ini, data_fin, \
                    concl, venc, adv, cliente, cliente_cpf, descricao, True, True


    # Fallback padrão
    return dash.no_update, [], {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, True

