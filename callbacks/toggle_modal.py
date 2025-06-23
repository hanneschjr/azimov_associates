from dash.dependencies import Input, Output, State, ALL
from app import app


# Abrir Modal Lawyers
@app.callback(
    Output('modal_lawyers', 'is_open'),
    Input('lawyers_button', 'n_clicks'),
    Input('quit_button', 'n_clicks'),
    Input('new_adv_button', 'n_clicks'),
    State('modal_lawyers', 'is_open')
)
def toggle_modal(n, n2, n3, is_open):
    if n or n2 or n3:
        return not is_open
    return is_open