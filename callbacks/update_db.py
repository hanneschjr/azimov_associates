from dash import Input, Output
import pandas as pd

# import from folders
from app import * 
from db.queries import add_adv



# Dcc.Store back to file
@app.callback(
    Output('div_fantasma', 'children'), 
    Input('store_adv', 'data'),
    Input('store_proc', 'data'),
)
def update_db(adv_data, proc_data):
    if not adv_data:
        return []

    row = adv_data[-1]
    add_adv(row['Advogado'], row['OAB'], row['CPF'])

    return []
