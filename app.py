# Arquivo app do Software de Gestão de Escritório de Advocacia - Pjt Azimov modificado
import dash
import dash_bootstrap_components as dbc


# onde pega os ícones e o tema LUX
# baixa os bootstrap templates que tem ligação com o LUX (só o css)
# a folha de estilos é o front-awesome + dbc.theme + css
estilos = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css', dbc.themes.LUX] 
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css" 
app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css]) 

# suprime o lançamentos de exceções que alguns callbacks podem conter
# informa oa Dash que ele deve servir seus arquivos JavaScript internamente, a partir do próprio servidor Flask (localmente)
# app é o app Desh, app.server é o app Flask interno e server = app.server torna disponível fora do Dash
app.config['suppress_callback_exceptions'] = True 
app.scripts.config.serve_locally = True 
server = app.server 

