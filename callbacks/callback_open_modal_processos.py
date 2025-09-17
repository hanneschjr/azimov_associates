from dash.dependencies import Input, Output, State
from app import app

# Abrir Modal Lawyers
@app.callback(
    Output('modal_processo', 'is_open'),
    Input('processo_button', 'n_clicks'),
    State('modal_processo', 'is_open'),
    prevent_initial_call=True
)
def open_modal_processo(n, is_open):
    print('Callback abrir modal processos iniciado ==============')
    if n:
        return not is_open
    return is_open