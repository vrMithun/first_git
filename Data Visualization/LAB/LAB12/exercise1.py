import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# --------------------
# Sample Data (replace with pd.read_csv("your_file.csv"))
# --------------------

df = pd.read_csv(r"D:\workspace\first_git\Data Visualization\LAB\LAB12\retail_sales_dataset.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract Month-Year
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# --------------------
# Dash App
# --------------------
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard", style={"textAlign": "center"}),

    # Dropdown filter
    html.Div([
        html.Label("Filter by Gender or Product Category:"),
        dcc.Dropdown(
            id="filter-dropdown",
            options=(
                [{"label": g, "value": g} for g in df["Gender"].unique()] +
                [{"label": c, "value": c} for c in df["Product Category"].unique()]
            ),
            value=None,
            placeholder="Select Gender or Product Category"
        )
    ], style={"width": "40%", "margin": "auto"}),

    # Summary Cards
    html.Div(id="summary-cards", style={"display": "flex", "justifyContent": "space-around", "marginTop": "20px"}),

    # Graphs
    html.Div([
        dcc.Graph(id="line-chart"),
        dcc.Graph(id="bar-chart"),
        dcc.Graph(id="pie-chart")
    ])
])


# --------------------
# Callbacks
# --------------------
@app.callback(
    [Output("line-chart", "figure"),
     Output("bar-chart", "figure"),
     Output("pie-chart", "figure"),
     Output("summary-cards", "children")],
    [Input("filter-dropdown", "value")]
)
def update_dashboard(filter_value):
    # Filtered Data
    dff = df.copy()
    if filter_value:
        if filter_value in dff["Gender"].unique():
            dff = dff[dff["Gender"] == filter_value]
        elif filter_value in dff["Product Category"].unique():
            dff = dff[dff["Product Category"] == filter_value]

    # Line chart: Monthly Sales Trend
    monthly_sales = dff.groupby("Month")["Total Amount"].sum().reset_index()
    line_fig = px.line(monthly_sales, x="Month", y="Total Amount", title="Monthly Sales Trend")

    # Bar chart: Sales by Product Category
    category_sales = dff.groupby("Product Category")["Total Amount"].sum().reset_index()
    bar_fig = px.bar(category_sales, x="Product Category", y="Total Amount", title="Sales by Product Category")

    # Pie chart: Sales by Gender
    gender_sales = dff.groupby("Gender")["Total Amount"].sum().reset_index()
    pie_fig = px.pie(gender_sales, names="Gender", values="Total Amount", title="Sales Distribution by Gender")

    # Summary Cards
    total_sales = dff["Total Amount"].sum()
    avg_order_value = dff.groupby("Transaction ID")["Total Amount"].sum().mean()
    top_product = dff.groupby("Product Category")["Total Amount"].sum().idxmax()

    cards = [
        html.Div([
            html.H3("Total Sales"),
            html.P(f"${total_sales:,.2f}")
        ], style={"border": "1px solid gray", "padding": "10px", "borderRadius": "10px"}),

        html.Div([
            html.H3("Avg Order Value"),
            html.P(f"${avg_order_value:,.2f}")
        ], style={"border": "1px solid gray", "padding": "10px", "borderRadius": "10px"}),

        html.Div([
            html.H3("Top Selling Product"),
            html.P(top_product)
        ], style={"border": "1px solid gray", "padding": "10px", "borderRadius": "10px"})
    ]

    return line_fig, bar_fig, pie_fig, cards


# --------------------
# Run Server
# --------------------
if __name__ == "__main__":
    app.run(debug=True)
