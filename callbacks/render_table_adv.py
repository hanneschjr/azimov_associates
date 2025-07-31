
from dash.dependencies import Input, Output
import pandas as pd

from dash import dash_table
from dash.dash_table.Format import Group

from app import app
from components import home

@app.callback(
    Output('table_adv', 'children'),
    Input('store_adv', 'data')
)
def render_table_adv(data):
    df = pd.DataFrame(data)
    df = df.fillna('-')
    return [
        dash_table.DataTable(
            id='datatable',
            columns= [{'name': i, 'id': i} for i in df.columns],
            data = df.to_dict('records'),
            page_size=10,
            page_current=0
        )
    ]
