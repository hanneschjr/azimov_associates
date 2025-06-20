import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

# init database
from db import init_db
init_db()

# import from folders
from app import * 
from components import home, sidebar
from db.connect import *
import pandas as pd
from db.queries import consulta_geral_advogados, consulta_geral_processos, add_adv

dados_adv = consulta_geral_advogados()
df_adv = pd.DataFrame(dados_adv, columns=['Advogado', 'OAB', 'CPF'])
print(df_adv)

dados_proc = consulta_geral_processos()
df_proc = pd.DataFrame(dados_proc, columns=['Nr Processo',
                                            'Empresa',
                                             'CPF',
                                             'Tipo',
                                             'Ação',
                                             'Vara',
                                             'Instância',
                                             'Data inicial',
                                             'Data final',
                                             'Processo Concluído',
                                             'Processo vencido',
                                             'Advogados',
                                             'Cliente',
                                             'CPF cliente',
                                             'Descrição'])

# Criar estrutura para Store intermediária ===============




# ====================== Layout =================== #
app.layout = dbc.Container([
    # Store e Location
    dcc.Location(id='url'),
    dcc.Store(id='store_intermedio', data={}),
    dcc.Store(id='store_adv', data=df_adv.to_dict('records')),
    dcc.Store(id='store_proc', data=df_proc.to_dict('records')),
    html.Div(id='div_fantasma'),

    # Layout
    dbc.Row([
        dbc.Col([
            sidebar.layout
        ], md=2, style={'padding': '0px'}),
        dbc.Col([
            dbc.Container(id='page-content', fluid=True, style={'height': '100%', 'width': '100%', 'padding-left': '14px'})
        ], md=10, style={'padding': '0px'})

    ])

], fluid=True)

# ====================== Callbacks =================== #
# URL callback to update page content
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def render_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
    else:
        return dbc.Container([
            html.H1('404: Not found', className='text-danger'),
            html.Hr(),
            html.P(f"O caminho '{pathname}' não foi reconhecido..."),
            html.P('Use a NavBar para retornar ao sistema de maneira correta.')
        ])



# Dcc.Store back to file
@app.callback(
    Output('div_fantasma', 'children'), 
    Input('store_adv', 'data'),
    Input('store_proc', 'data'),
)
def update_file(adv_data, proc_data):
    if not adv_data:
        return []

    df_adv_aux = pd.DataFrame(adv_data)
    df_proc_aux = pd.DataFrame(proc_data) if proc_data else pd.DataFrame()

    for _, row in df_adv_aux.iterrows():
        add_adv(row['Advogado'], row['OAB'], row['CPF'])

    return []


if __name__ == '__main__':
    app.run(debug=True, port=8050, host='0.0.0.0')






