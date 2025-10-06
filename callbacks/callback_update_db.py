from dash import Input, Output, State
import pandas as pd
from time import sleep

# import from folders
from app import * 
from db.queries import add_adv, add_proc



# Dcc.Store back to file
@app.callback(
    Output('div_fantasma', 'children'),
    Input('store_adv', 'data'),
    Input('store_proc', 'data'),
    State('input_no_processo', 'disable'),
    prevent_initial_call=True
)
def update_db_adv(adv_data, proc_data, disable):
    df_adv_aux = pd.DataFrame(adv_data, columns=['Advogado', 'OAB', 'CPF'])
    df_proc_aux = pd.DataFrame(proc_data, columns= ['Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase', 'Instância',
                                                    'Data Inicial', 'Data Final', 'Processo Concluído', 'Processo Vencido',
                                                    'Advogado', 'Cliente', 'CPF Cliente', 'Descrição'])
    # df_int_aux = pd.DataFrame(int_data, columns=['Nr Processo', 'Empresa', 'Tipo', 'Ação', 'Vara', 'Fase', 'Instância',
    #                                                 'Data Inicial', 'Data Final', 'Processo Concluído', 'Processo Vencido',
    #                                                 'Advogado', 'Cliente', 'CPF Cliente', 'Descrição', 'disable'])
    if not adv_data:
        pass
    else:
        row_adv = adv_data[-1]
        add_adv(row_adv['Advogado'], row_adv['OAB'], row_adv['CPF'])
   


    if not proc_data:
        pass
    elif not disable: # inserir registro novo
        row_proc = proc_data[-1]
        add_proc(row_proc['Nr Processo'], row_proc['Empresa'], row_proc['Tipo'],
                row_proc['Ação'], row_proc['Vara'], row_proc['Fase'],
                row_proc['Instância'], row_proc['Data Inicial'], row_proc['Data Final'],
                row_proc['Processo Concluído'], row_proc['Processo Vencido'], row_proc['Advogado'],
                row_proc['Cliente'], row_proc['CPF Cliente'], row_proc['Descrição'],)
        
        print('Callback de insersão do item na base de dados acioando! =========')
        sleep(5)

    elif disable: # update (edição)
       df_proc_aux.loc[df_proc_aux['Nr Processo'] == df_int_aux['Nr Processo'][0]] 
    
    return []