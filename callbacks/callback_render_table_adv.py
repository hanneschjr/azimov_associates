from dash.dependencies import Input, Output
import pandas as pd
from dash import dash_table


from app import app
from components import home

@app.callback(
    Output('table_adv', 'children'),
    Input('store_adv', 'data'),
    prevent_initial_call=True
)
def render_table_adv(data):
    print('O callback de renderização da tabela foi acionado! =============')
    # print(f'{data}')
    df = pd.DataFrame(data)
    return [
        dash_table.DataTable(
            id='datatable',
            columns= [{'name': i, 'id': i} for i in df.columns],
            data = df.to_dict('records'),
            page_size=10,
            page_current=0
        )
    ]

