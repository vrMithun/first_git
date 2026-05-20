import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Mastering Streamlit - Step 4",
    page_icon="⚡",
    layout="centered"
)

st.title("Step 4: Dynamic Data Filtering & Reactive State")
st.caption("Filenamed: 04_dynamic_data_filtering.py | Target: Binding user variables directly to data queries")

@st.cache_data
def generate_large_sales_pipeline():
    """Generates 500 rows of randomized global sales records."""
    np.random.seed(101)
    row_count = 500
    
    products = ["Enterprise Cloud License", "Hardware Router v2", "AI API Token Packs", "Premium Security Suite"]
    regions = ["North America", "Europe", "Asia-Pacific", "Latin America"]
    channels = ["Direct Sales", "Online Store", "Reseller Partner"]
    
    df = pd.DataFrame({
        "Order_ID": [f"ORD-{i+1000}" for i in range(row_count)],
        "Product": np.random.choice(products, size=row_count),
        "Region": np.random.choice(regions, size=row_count),
        "Channel": np.random.choice(channels, size=row_count),
        "Units_Sold": np.random.randint(1, 50, size=row_count),
        "Unit_Price_USD": np.random.choice([150, 450, 1200, 3500], size=row_count, p=[0.4, 0.3, 0.2, 0.1])
    })
    
    # Calculate revenue extensions
    df["Total_Revenue_USD"] = df["Units_Sold"] * df["Unit_Price_USD"]
    return df

raw_sales_df = generate_large_sales_pipeline()

st.header("1. Dashboard Filter Controls")
st.write("Adjust these parameters below. Watch how the entire database queries itself reactively.")

search_query = st.text_input("🔍 Search by Product Name Keyword", value="")

all_regions = list(raw_sales_df["Region"].unique())
selected_regions = st.multiselect("🌐 Filter by Region Target", options=all_regions, default=all_regions)

max_transaction_value = int(raw_sales_df["Total_Revenue_USD"].max())
revenue_range = st.slider(
    label="💵 Total Transaction Revenue Window ($)",
    min_value=0,
    max_value=max_transaction_value,
    value=[0, max_transaction_value] # Initial state spanning the full width
)

st.divider()

filtered_df = raw_sales_df.copy()

# Step A: Filter by Text Search String
if search_query:
    filtered_df = filtered_df[filtered_df["Product"].str.contains(search_query, case=False)]

# Step B: Filter by Selected Regions List
filtered_df = filtered_df[filtered_df["Region"].isin(selected_regions)]

# Step C: Filter by Slider Range Bounds
filtered_df = filtered_df[
    (filtered_df["Total_Revenue_USD"] >= revenue_range[0]) & 
    (filtered_df["Total_Revenue_USD"] <= revenue_range[1])
]

st.header("2. Live Dynamic Summary Metrics")

# Calculate metrics from our newly filtered dataframe subset, not the raw baseline
total_filtered_revenue = filtered_df["Total_Revenue_USD"].sum()
total_units_moved = filtered_df["Units_Sold"].sum()
active_deal_count = len(filtered_df)

# Render KPI cards that update in lockstep with the filters
st.metric(label="Total Aggregated Revenue", value=f"${total_filtered_revenue:,.2f}")
st.metric(label="Total Units Transacted", value=f"{total_units_moved:,}")
st.metric(label="Total Unique Matching Deals", value=f"{active_deal_count}")

st.divider()

st.header("3. Filtered Data & Analytics Visualization")

if filtered_df.empty:
    st.error("❌ No transactions match your current filtering criteria. Please expand your constraints.")
else:
    # Render table view of matched rows
    st.subheader("Isolated Transaction Ledger")
    st.dataframe(filtered_df, use_container_width=True)
    
    # Generate an on-the-fly aggregation chart grouping revenue by item type
    st.subheader("Aggregated Revenue Contributed per Product")
    chart_data = filtered_df.groupby("Product")["Total_Revenue_USD"].sum()
    st.bar_chart(chart_data)

