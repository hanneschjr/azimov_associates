import dash
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL
import dash_bootstrap_components as dbc

import json
import pandas as pd

from components import modal_advogados, modal_novo_advogado, modal_processo
from app import app

# =========== Layout ========== #
layout = dbc.Container([
    modal_novo_advogado.layout,
    modal_processo.layout,
    modal_advogados.layout,
    dbc.Container([
        
    ])
])




# ========= Callbacks =========== #
# Abrir Model New Lawyer




# Abrir Modal Lawyers