from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 1. Initialize the Dash app
app = Dash(__name__)

# 2. Load the dataset
df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by="Date")

# 3. Create the Line Chart using Plotly Express
fig = px.line(
    df, 
    x="Date", 
    y="Sales", 
    title="Pink Morsel Sales Over Time"
)

# 4. Define the App Layout (HTML structure)
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualizer', style={'textAlign': 'center'}),

    html.Div(children='''
        Visualizing sales data to analyze the impact of the price increase on Jan 15, 2021.
    ''', style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

# 5. Run the App
if __name__ == '__main__':
    app.run(debug=True)