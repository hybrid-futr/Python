# Run this app with `python app2.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/jfremzrai/Python/master/spam/surveys.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='Portal Teaching Data'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)