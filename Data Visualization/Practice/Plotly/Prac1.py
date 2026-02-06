import plotly.express as px
import dash

# Initialize app
app = dash.Dash(__name__)


df=px.data.gapminder()
df_sub = df[df['country'].isin(['India', 'China', 'United States'])]

fig = px.line(
    df_sub,
    x='year',
    y='lifeExp',
    color='country',           # separate lines by country
    markers=True,              # show markers at each data point
    title='Life expectancy over time',
    labels={'year':'Year', 'lifeExp':'Life expectancy (years)'},
    hover_name='country'       # show country name prominently on hover
)

fig.update_layout(template='plotly_white')  # clean background
fig.show()

# If you want a standalone file you can open in a browser:
#fig.write_html("life_expectancy.html", include_plotlyjs='cdn')