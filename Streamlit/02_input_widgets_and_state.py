import streamlit as st
import datetime

st.set_page_config(
    page_title="Mastering Streamlit - Step 2",
    page_icon="🎛️",
    layout="centered"
)

st.title("Step 2: Interactive Input Widgets & State Capture")
st.caption("Filenamed: 02_input_widgets_and_state.py | Target: Full control over user inputs")

st.header("1. Text & Numeric Inputs")
user_profile_name = st.text_input(
    label="Profile Name / Client ID",
    value="Guest_User", # Default value
    max_chars=20,
    help="Enter a unique identifier for your dashboard tracking."
)

api_key = st.text_input("Enter Data API Key", type="password")
threshold_limit = st.number_input(
    label="Alert Threshold Limit (Float)",
    min_value=0.0,
    max_value=100.0,
    value=75.5,
    step=0.5
)

st.divider()

st.header("2. Selection & Range Controls")
age_selection = st.slider("Select User Age Range", min_value=18, max_value=100, value=30)
min_price, max_price = st.slider(
    label="Select Price Range Target ($)",
    min_value=0,
    max_value=1000,
    value=[200, 800] # Returns a list of two values
)

data_source = st.selectbox(
    label="Choose Data Connection Source",
    options=["Production SQL Server", "Staging Environment", "Local CSV Cache", "Mock API Pipeline"]
)

target_regions = st.multiselect(
    label="Select Analysis Regions (Multi)",
    options=["North America", "Europe", "Asia-Pacific", "Latin America", "Africa"],
    default=["North America", "Europe"] # Initial items selected
)
st.divider()

st.header("3. Boolean Toggles & Date Pickers")
enable_analytics = st.checkbox("Enable Advanced Analytics Overlay", value=True)
dark_mode_sim = st.toggle("Simulate High-Contrast UI Mode")
selected_date = st.date_input(
    label="Target Audit Date",
    value=datetime.date(2026, 5, 20),
    min_value=datetime.date(2020, 1, 1)
)

st.divider()

st.header("4. Action Trigger (The Button)")
st.write("Buttons do NOT save state. They return `True` *only* on the exact rerun they are clicked.")
run_audit = st.button("Generate Configuration Audit Report", type="primary")
st.divider()

st.header("5. Dynamic State Output Panel")
st.write("Notice how the variables below change instantly as you adjust the controls above.")

if run_audit:
    st.success("✅ Audit Report successfully compiled below!")
    
    # We display our collected Python variables inside a clean JSON schema
    live_state = {
        "Profile Name": user_profile_name,
        "API Key Hidden length": len(api_key),
        "Threshold": threshold_limit,
        "Age Set": age_selection,
        "Price Window": [min_price, max_price],
        "Source Chosen": data_source,
        "Regions Selected": target_regions,
        "Analytics Enabled": enable_analytics,
        "High-Contrast On": dark_mode_sim,
        "Target Date Object": str(selected_date)
    }
    
    st.json(live_state)
else:
    st.info("ℹ️ Click the primary button above to lock in variables and generate the JSON summary.")