from dash import html
import dash_bootstrap_components as dbc
# from utils.icons_gen import gerar_icone

def gerar_card_processo(df_aux, color_c, color_v, concluido, vencido, concluido_text, vencido_text):
    card_style = {'height': '100%', 'margin-bottom': '12px'}
    card_processo = dbc.Card([
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            html.H2(f"Processo nº {df_aux['Nr Processo']}")
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.P("Processo corre em segredo de justiça por questões similares.", style={'text-align': 'left'})
                        ])
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.Ul([
                                html.Li([html.B("DATA: ", style={'font-weight': 'bold'}), f"{df_aux['Data Inicial']} - {df_aux['Data Final']}"]),
                                html.Li([html.B("AÇÃO: ", style={'font-weight': 'bold'}), f"{df_aux['Ação']}"]),
                                html.Li([html.B("INSTÂNCIA: ", style={'font-weight': 'bold'}), f"{df_aux['Instância']}"]),
                                html.Li([html.B("FASE: ", style={'font-weight': 'bold'}), f"{df_aux['Fase']}"]),
                                html.Li([html.B("DESCRIÇÃO: ", style={'font-weight': 'bold'}), f"{df_aux['Descrição']}"]),
                            ])
                        ])
                    ])
                ], sm=12, md=6, style={'border-right': '2px solid lightgrey'}),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            html.Ul([
                                html.Li([html.B("CLIENTE: ", style={'font-weight': 'bold'}), f"{df_aux['Cliente']}"]),
                                html.Li([html.B("EMPRESA: ", style={'font-weight': 'bold'}), f"{df_aux['Empresa']}"]),
                                html.Li([html.B("ADVOGADO: ", style={'font-weight': 'bold'}), f"{df_aux['Advogado']}"]),
                            ])
                        ])
                    ], style={'margin-bottom': '32px'}),
                    dbc.Row([
                        dbc.Col([
                            html.H5("STATUS", style={'margin-bottom':0}),
                        ], sm=5, style={'text-align': 'right'}),
                        dbc.Col([
                            html.I(className=f'{concluido} fa-2x dbc', style={'color': f'{color_c}'}),
                        ], sm=2),
                        dbc.Col([
                            html.H5(f"{concluido_text}", style={'margin-bottom': 0}),
                        ], sm=5, style={'text-align': 'left'}),
                    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                    dbc.Row([
                        dbc.Col([
                            html.H5("RESULTADO", style={'margin-bottom':0}),
                        ], sm=5, style={'text-align': 'right'}),
                        dbc.Col([
                            html.I(className=f'{vencido} fa-2x dbc', style={'color': f'{color_v}'}),
                        ], sm=2),
                        dbc.Col([
                            html.H5(f"{vencido_text}", style={'margin-bottom': 0}),
                        ], sm=5, style={'text-align': 'left'}),
                    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button([html.I(className='fa fa-pencil fa-2x')], style={'color': 'black'}, size='sm', outline=True, 
                                       id={'type': 'editar_processo', 'index': int(df_aux['Nr Processo'])}),
                        ], sm=2),
                        dbc.Col([
                            dbc.Button([html.I(className='fa fa-trash fa-2x')], style={'color': 'black'}, size='sm', outline=True, 
                                       id={'type': 'deletar_processo', 'index': int(df_aux['Nr Processo'])}),
                        ], sm=2),
                    ], style={'display': 'flex', 'justify-content': 'flex-end'}),                                  
                ], sm=12, md=6, style={'height': '100%', 'margin-top': 'auto', 'margin-bottom': 'auto'})
            ], style={'margin-top': '12px'})

        ])
    ], style=card_style, className='card_padrao')

    return card_processo