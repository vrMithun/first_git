# 03_data_and_charts.py
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Mastering Streamlit - Step 3",
    page_icon="📊",
    layout="centered"
)

st.title("Step 3: High-Performance Data Display & Native Charting")
st.caption("Filenamed: 03_data_and_charts.py | Target: Complete mastery over tabular data and plotting")
@st.cache_data
def generate_mock_financial_data():
    np.random.seed(42)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    df = pd.DataFrame({
        'Month': months,
        'Revenue_USD': np.random.randint(45000, 95000, size=12),
        'Operational_Cost': np.random.randint(30000, 55000, size=12),
        'Customer_Count': np.random.randint(1200, 3500, size=12),
        'Region': np.random.choice(['North', 'East', 'South', 'West'], size=12)
    })
    
    # Calculate engineering columns
    df['Net_Profit'] = df['Revenue_USD'] - df['Operational_Cost']
    df['Profit_Margin_%'] = round((df['Net_Profit'] / df['Revenue_USD']) * 100, 1)
    
    return df.set_index('Month')
financial_df = generate_mock_financial_data()

st.header("1. Tabular Data Presentation")

st.subheader("The Interactive DataFrame Container (`st.dataframe`) ")
st.write("Best for deep data exploration. Users can sort columns, resize boundaries, and download CSVs.")

st.dataframe(
    data=financial_df,
    height=300,
    use_container_width=True # Stretches to fill the layout block
)

st.subheader("The Conditional Styler Panel")
st.write("You can inject Pandas `.style` objects directly into Streamlit to build heatmaps.")
styled_df = financial_df.style.highlight_max(axis=0, color="#d4e9ed")\
                    .background_gradient(subset=['Profit_Margin_%'], cmap='YlOrRd')

st.dataframe(styled_df, use_container_width=True)

st.subheader("The Static Report Table (`st.table`)")
st.write("Warning: This strips all interactivity and renders a heavy, fixed HTML table. Use sparingly.")
st.table(financial_df.head(3)) # Only showing 3 rows to protect vertical space

st.divider()

st.header("2. Built-in Analytics & Plotting Engines")
st.write("Streamlit features native plotting elements that read Pandas indexes automatically as the X-axis.")

st.subheader("Multi-Series Line Chart (`st.line_chart`)")

chart_columns = ['Revenue_USD', 'Operational_Cost', 'Net_Profit']
st.line_chart(data=financial_df[chart_columns])

st.subheader("Comparative Bar Chart (`st.bar_chart`)")
st.bar_chart(data=financial_df[['Customer_Count']])

st.subheader("Area Charts for Volume Visualizations (`st.area_chart`)")
st.area_chart(data=financial_df[['Net_Profit']])