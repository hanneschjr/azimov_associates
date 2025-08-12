import dash
from dash.dependencies import Input, Output
import pandas as pd

from dash import dash_table
from dash.dash_table.Format import Group

from app import app
from components import home

@app.callback(
    Output('advogados_envolvidos', 'options'),
    Input('store_adv', 'data')
)
def fill_drop_adv(data):
    df = pd.DataFrame(data)
    adv_list = list(df['Advogado'])
    return adv_list
