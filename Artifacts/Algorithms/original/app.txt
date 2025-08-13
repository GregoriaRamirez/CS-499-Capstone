from dash import Dash
from view import layout
from controller import register_callbacks

app = Dash(__name__)
app.layout = layout

# Register all callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True, port=8550)
