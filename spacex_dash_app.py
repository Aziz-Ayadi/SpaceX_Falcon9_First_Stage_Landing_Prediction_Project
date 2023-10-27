# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("Data-Wrangling-Dataset.csv")
max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # Adding a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown', 
                                options=[{'label': 'All Sites', 'value': 'ALL'},
                                {'label': 'CCSFS SLC 40', 'value': 'CCSFS SLC 40'},
                                {'label': 'VAFB SLC 4E', 'value': 'VAFB SLC 4E'},
                                {'label': 'KSC LC 39A', 'value': 'KSC LC 39A'}],
                                value='ALL',
                                placeholder='Select a Launch Site here',
                                searchable=True),
                                html.Br(),

                                # Adding a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for that site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg): "),
                                # Adding a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                min=0, max=10000, step=1000,
                                marks={0 : '0',
                                       100 : '100'},
                                value=[min_payload, max_payload]),

                                # Adding a scatter chart to show the correlation between payload mass and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output

@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='Class', 
        names='LaunchSite', 
        title='Total Success Launches By Sites')
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == str(entered_site)]
        fig = px.pie(filtered_df, values='Class', 
        names='Class',
        title='Total Success Launches By Site ' + entered_site)
    return fig

# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output

@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
[Input(component_id='site-dropdown', component_property='value'),
Input(component_id="payload-slider", component_property="value")])
def get_scatter_plot(entered_site, payload_mass):
    low, high = payload_mass
    filtered_df = spacex_df[(spacex_df['PayloadMass'] > low) & (spacex_df['PayloadMass'] < high)]
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='PayloadMass',
        y='Class', color='BoosterVersion',
        title='Correlation between Payload and Success for all Sites')
    else:
        fig = px.scatter(filtered_df[filtered_df['LaunchSite'] == str(entered_site)],
        x='PayloadMass', y='Class', color='BoosterVersion',
        title='Correlation between Payload and Success for Site ' + entered_site)
    return fig

# Run the app

if __name__ == '__main__':
    app.run_server()
