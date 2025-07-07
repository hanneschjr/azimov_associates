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

    df_adv_aux = pd.DataFrame(adv_data)
    df_proc_aux = pd.DataFrame(proc_data) if proc_data else pd.DataFrame()

    for _, row in df_adv_aux.iterrows():
        add_adv(row['Advogado'], row['OAB'], row['CPF'])

    return []
