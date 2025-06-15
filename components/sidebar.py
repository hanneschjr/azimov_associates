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
    # modal_novo_advogado.layout,
    # modal_processo.layout,
    # modal_advogados.layout,
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("ASIMOV", style={'color': 'yellow'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.H3("ASSOCIATES", style={'color': 'white'})
            ]),
        ]),
    ], 
    style={'padding-top': '50px', 'margin-bottom': '100px'}, className='text-center'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Nav([
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-home dbc'), "\tINÍCIO"], href="/home", active=True, style={'text-align': 'left'})),
                html.Br( ),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-plus-circle dbc'), "\tPROCESSOS"], id='processo_button', active=True, style={'text-align': 'left'})),
                html.Br( ),
                dbc.NavItem(dbc.NavLink([html.I(className='fa fa-user-plus dbc'), "\tADVOGADOS"], id='laweyers_button', active=True, style={'text-align': 'left'})),
            ], vertical='lg', pills=True, fill=True)
            
        ])
    ])
], style={'height':'100vh', 'padding': '0px', 'position': 'sitcky', 'top': 0, 'background-color': '#232423'})




# ========= Callbacks =========== #
# Abrir Model New Lawyer




# Abrir Modal Lawyers