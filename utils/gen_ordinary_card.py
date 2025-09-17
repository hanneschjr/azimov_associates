from dash import html
import dash_bootstrap_components as dbc

def gerar_card_processo(df_aux, color_c, color_v, concluido, vencido, concluido_text, vencido_text):
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
                                html.Li([html.B("DATA: ", style={'font-weight': 'bold'}), f"{df_aux['Data inicial']} - {df_aux['Data final']}"]),
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
                                html.Li([html.B("ADVOGADO: ", style={'font-weight': 'bold'}), f"{df_aux['Empresa']}"]),
                            ])
                        ])
                    ])
                    
                ], sm=12, md=6, style={'height': '100%', 'margin-top': 'auto', 'margin-bottom': 'auto'})
            ])

        ])
    ])