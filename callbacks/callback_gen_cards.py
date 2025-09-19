from dash import html, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import pandas as pd
from utils.std_count_card_gen import gerar_card_padrao
from utils.icons_gen import gerar_icones
from utils.gen_ordinary_card import gerar_card_processo
# import from folders
from app import * 

# Este callback irá controlar os campos de filtro do respectivo card
@app.callback(
    Output('card_generator', 'children'), # é um container dentro do layout de home
    Output('advogados_filter', 'value'), # é o atributo value do dropdown filtro advogado (também é um Input)
    Output('processos_filter', 'value'), # se refere ao Input do nº do processo (também é um State)
    Output('input_cpf_pesquisa', 'value'), # se refere ao Input do CPF (também é um State)
    Input('pesquisar_cpf', 'n_clicks'), # se refere ao botão de busca
    Input('todos_processos', 'n_clicks'), # se refere ao botão Todos os Processo
    Input('advogados_filter', 'value'), # ao dropdown Advogado (também é um Output)
    Input('pesquisar_num_proc', 'n_clicks'), # ao botão de busca (Lupa)
    Input('store_proc', 'data'), # é o store de processos
    Input('store_adv', 'data'), # é o store de advogados
    Input('switches_input', 'value'), # é o checklist switch de status do processo
    Input('checklist_input', 'value'), # é o checklist de instância
    State('processos_filter', 'value'), # é o Input (também é um Output)
    State('input_cpf_pesquisa', 'value') # é o Input do CPF (também é um Output)
)
def generate_cards(n, n_all, adv_filter, proc_button, proc_data, adv_data, switches, checklist, proc_filter, cpf)
    trigg_id = callback_context.triggered[0]['prop_id'].split('.')[0]

    # Iniciar os cards 
    cards = []

    # Iniciar possíveis dataframes

    df_adv_aux = pd.DataFrame(adv_data)
    df_proc_aux = pd.DataFrame(proc_data)

    if (trigg_id == '' or trigg_id == 'store_proc' or trigg_id == 'store_adv' or trigg_id == 'todos os processos' or trigg_id == 'checklist_input'):
        if trigg_id != 'todos_processos':
            # Filtros dos switches
            if (1 and 2) in switches:
                df_proc_aux = df_proc_aux.loc[(df_proc_aux['Processo Concluído'] == 1) & (df_proc_aux['Processo Vencido'] == 1)]
            elif switches == [1]:
                df_proc_aux = df_proc_aux.loc[df_proc_aux['Processo Concluído'] == 1]
            elif switches == [2]:
                df_proc_aux = df_proc_aux.loc[df_proc_aux['Processo Vencido'] == 1]
            
            if (1 in checklist) and (2 in checklist): pass
            elif checklist == [1]: df_proc_aux = df_proc_aux.loc[df_proc_aux['Instância'] == 1]
            elif checklist == [2]: df_proc_aux = df_proc_aux.loc[df_proc_aux['Instância'] == 2]
        
        df_proc_aux = df_proc_aux.sort_values(by='Data Inicial', ascending=False)

        df_proc_aux.loc[df_proc_aux['Processo Concluído'] == 0, 'Processo Concluído'] = 'Não'
        df_proc_aux.loc[df_proc_aux['Processo Concluído'] == 1, 'Processo Concluído'] = 'Sim'
        df_proc_aux.loc[df_proc_aux['Processo Vencido'] == 0, 'Processo Concluído'] = 'Não'
        df_proc_aux.loc[df_proc_aux['Processo Vencido'] == 1, 'Processo Concluído'] = 'Sim'

        df_proc_aux = df_proc_aux.fillna('-')

        # inserir o card padrão
        qnt_proc = len(df_proc_aux)
        cards += [gerar_card_padrao(qnt_proc)]

        for i in range(qnt_proc):
            df_aux, concluido, vencido, color_c, color_v, concluido_text, vencido_text = gerar_icones(df_proc_aux, i)
            card = gerar_card_processo(df_aux, color_c, color_v, concluido, vencido, concluido_text, vencido_text)
            cards += card

        return cards, None, None, None