# Arquivo de inicialização do Software de Gestão de Escritório de Advocacia - Azimov
import dash
import dash_bootstrap_components as dbc

estilos = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/front-awesome.min.css', dbc.themes.LUX] # onde pega os ícones e o tema LUX
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css" # baixa os bootstrap templates que tem ligação com o LUX (só o css)

app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css]) # a folha de estilos é o front-awesome + dbc.theme + css

app.config['suppress_callback_exceptions'] = True # suprime o lançamentos de exceções que alguns callbacks podem conter
app.scripts.config.serve_locally = True # informa oa Dash que ele deve servir seus arquivos JavaScript internamente, a partir do próprio servidor Flask (localmente)
server = app.server # app é o app Desh, app.server é o app Flask interno e server = app.server torna disponível fora do Dash

