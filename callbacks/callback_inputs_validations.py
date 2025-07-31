import dash 
from dash import Input, Output, State, callback_context
from app import app
from utils.inputs_validates import validar_cpf

# validação dos campos do formulário "Novo Advogado" e do botão "Salvar"
@app.callback(
    Output('save_button_novo_advogado', 'disabled'),
    Output('adv_oab', 'valid'),
    Output('adv_cpf', 'valid'),
    Output('adv_nome', 'valid'),
    Input('adv_oab', 'value'),
    Input('adv_cpf', 'value'),
    Input('adv_nome', 'value'),
)
def validation_inputs(val_oab, val_cpf, val_name):
    ctx = callback_context
    if not ctx.triggered:
        return dash.no_update, dash.no_update, dash.no_update
        # Detecta qual botão foi clicado
        
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # if n or n2 or n3:
    #     return not is_open
    # return is_open