from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. Initialize the Dash app
app = Dash(__name__)

# 2. Load and Sort the dataset
df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by="Date")

# 3. Define the App Layout
app.layout = html.Div(children=[
    
    # Header
    html.H1(children='Pink Morsel Sales Visualizer'),

    html.Div(children='Select a region to analyze sales trends:', style={'textAlign': 'center', 'marginBottom': '10px'}),

    # Radio Button for Filtering
    html.Div(
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All Regions', 'value': 'all'}
            ],
            value='all',  # Default selection
            className='radio-group' # Uses the CSS class we defined
        )
    ),

    # The Graph Container
    html.Div(
        dcc.Graph(id='sales-graph'),
        className='graph-container'
    )
])

# 4. Create the Callback (Interaction Logic)
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Logic: If 'all' is selected, use the full dataframe.
    # Otherwise, filter the dataframe by the selected region.
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    # Create the figure with the filtered data
    fig = px.line(
        filtered_df, 
        x="Date", 
        y="Sales", 
        title=f"Sales in {selected_region.capitalize()} Region" if selected_region != 'all' else "Sales in All Regions"
    )
    
    # Update the layout of the graph specifically
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#333'
    )
    
    return fig

# 5. Run the App
if __name__ == '__main__':
    app.run(debug=True)