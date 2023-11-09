import pandas as pd
import plotly.express as px

server = app.server
def index():
    # Read the population data from CSV
    df = pd.read_csv('population.csv')

    # Create a choropleth map
    fig = px.choropleth(df,
                        locations='Country Name',
                        locationmode='country names',
                        color='Count',
                        color_continuous_scale='Blues',
                        title='Population Choropleth Map',
                        labels={'Count': 'Population'},
                        animation_frame="Year")

    fig.update_layout(
        updatemenus=[
            dict(
                type='buttons',
                showactive=False,
                buttons=[
                    dict(
                        label='Play',
                        method='animate',
                        args=[None, {
                            'frame': {'duration': 500, 'redraw': True},
                            'fromcurrent': True,
                            'transition': {'duration': 0}
                        }]
                    ),
                    dict(
                        label='Pause',
                        method='animate',
                        args=[[None], {
                            'frame': {'duration': 0, 'redraw': False},
                            'mode': 'immediate',
                            'transition': {'duration': 0}
                        }]
                    )
                ],
                direction='right',
                pad={'r': 10, 't': 10},
                x=0.1,
                xanchor='left',
                y=0,
                yanchor='top'
            ),
        ],
        sliders=[
            dict(
                active=0,
                steps=[
                    dict(
                        label=str(year),
                        method='animate',
                        args=[[year], {
                            'frame': {'duration': 500, 'redraw': True},
                            'mode': 'immediate',
                            'transition': {'duration': 0}
                        }]
                    )
                    for year in df['Year'].unique()
                ],
                pad={'t': 50}
            )
        ]
    )

    fig.show()
