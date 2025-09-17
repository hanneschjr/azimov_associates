import pandas as pd

def gerar_icone(df_proc_aux, i):
    df_aux = df_proc_aux.iloc[i]
    if df_aux['Processo Concluído'] == 'Sim' and df_aux['Processo Vencido'] == 'Sim':
        concluido = vencido = 'fa fa-check'
        color_c = color_v = 'green'
        concluido_text = 'Concluído'
        vencido_text = 'Vencido'
    elif df_aux['Processo Concluído'] == 'Sim' and df_aux['Processo Vencido'] == 'Não':
        concluido = 'fa fa-check'
        vencido = 'fa fa-times'
        color_c = 'green'
        color_v = 'red'
        concluido_text = 'Concluído'
        vencido_text = 'Perdido'
    elif df_aux['Processo Concluído'] == 'Não':
        concluido = vencido = 'fa fa-times'
        color_c = 'red'
        color_v = 'gray'
        concluido_text = vencido_text = 'Em andamento'

    return df_aux, concluido, vencido, color_c, color_v, concluido_text, vencido_text
      