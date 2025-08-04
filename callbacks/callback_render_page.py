from dash import html, Input, Output
import dash_bootstrap_components as dbc

# import from folders
from app import * 
from components import home


# ====================== Callbacks =================== #
# URL callback to update page content
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname')
)
def render_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
    else:
        return dbc.Container([
            html.H1('404: Not found', className='text-danger'),
            html.Hr(),
            html.P(f"O caminho '{pathname}' não foi reconhecido..."),
            html.P('Use a NavBar para retornar ao sistema de maneira correta.')
        ])
