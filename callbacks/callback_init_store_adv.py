from dash import Input, Output, callback
from app import app, cache

@callback(
    Output('store_adv', 'data'),
    Input('url', 'pathname'),  # disparo único ao abrir a app
    prevent_initial_call=False  # queremos rodar na inicialização
)
def init_store_adv(_):
    """
    Inicializa o dcc.Store 'store_adv' com os dados do cache/BD.
    """
    # get_advogados() é decorado com @cache.cached
    df = cache.get("advogados")
    print(df)
    if df is None:
        print('inicializei o store_adv')
        from db.queries import consulta_geral_advogados
        import pandas as pd
        dados_adv = consulta_geral_advogados()
        df = pd.DataFrame(dados_adv, columns=['Advogado', 'OAB', 'CPF'])
        cache.set("advogados", df, timeout=0)  # salva no Redis
    return df.to_dict("records")