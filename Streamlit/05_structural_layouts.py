import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Mastering Streamlit - Step 5",
    page_icon="📐",
    layout="wide" 
)

st.title("Step 5: Structural Layouts, Sidebars, and Containers")
st.caption("Filenamed: 05_structural_layouts.py | Target: Complete structural architecture mastery")

st.sidebar.header("🛠️ Dashboard Global Controls")
st.sidebar.write("This panel isolates input configurations away from your clean data displays.")

selected_department = st.sidebar.selectbox(
    "Select Corporate Department",
    ["Engineering", "Marketing", "Sales", "Human Resources"]
)

budget_allowance = st.sidebar.slider(
    "Set Target Department Budget ($k)", 
    min_value=10, max_value=500, value=250, step=10
)

# A status element in the sidebar to show it tracks state exactly the same way
st.sidebar.info(f"Current View: **{selected_department}**")

st.header("1. Horizontal Metric Layouts")
st.write("Instead of stacking your KPI cards vertically, wrap them inside `st.columns` to create an executive summary layout.")

# Create 3 columns by passing an integer. You get a list of column objects back.
col1, col2, col3 = st.columns(3)

# Use python's 'with' statement to target and render elements inside a specific column
with col1:
    st.metric(label=f"{selected_department} Target Allocations", value=f"${budget_allowance},000")

with col2:
    # Let's run a calculation based on the sidebar slider input
    spent_mock = int(budget_allowance * 0.72)
    st.metric(label="Current Capital Spent", value=f"${spent_mock},000", delta="-28% Budget Left")

with col3:
    burn_rate = "Stable" if budget_allowance > 200 else "Aggressive"
    st.metric(label="Operational Burn Profile", value=burn_rate)

st.divider()

st.header("2. Tabbed Content Containers")
st.write("Tabs allow you to keep your dashboard clean by hiding secondary views behind navigation clicks.")

tab_table, tab_chart, tab_documentation = st.tabs(["📋 Data Matrix View", "📈 Data Visualization", "📖 Architecture Docs"])

np.random.seed(42)
mock_timeline = pd.DataFrame({
    'Project Qtr': ['Q1-26', 'Q2-26', 'Q3-26', 'Q4-26'],
    'Projected_Output': np.random.randint(50, 100, size=4),
    'Actual_Output': np.random.randint(40, 110, size=4)
}).set_index('Project Qtr')

# Inject content to tab 1
with tab_table:
    st.subheader(f"Raw Project Matrices for {selected_department}")
    st.dataframe(mock_timeline, use_container_width=True)

# Inject content to tab 2
with tab_chart:
    st.subheader(f"Performance Tracking Timeline")
    st.line_chart(mock_timeline)

# Inject content to tab 3
with tab_documentation:
    st.subheader("Internal Metric Specifications")
    st.markdown("""
    This panel documents how system trackers scale across business logic lines.
    - **Target Allocations**: Set via the administrator global sidebar rig.
    - **Burn Profile**: Automatically flags as *Aggressive* if total runway sinks below $200k.
    """)

st.divider()

st.header("3. Collapsible Metadata Containers")

# st.expander builds a clickable dropdown toggle block. Perfect for audit logs or deep code summaries.
with st.expander("🔍 Click here to reveal raw backend application runtime environment state"):
    st.write("This section remains collapsed by default, preventing screen clutter for your end-users.")
    env_snapshot = {
        "Target Department Selected": selected_department,
        "Assigned Slider Value": budget_allowance,
        "Page Configuration Mode": "wide",
        "Framework State": "Healthy"
    }
    st.json(env_snapshot)