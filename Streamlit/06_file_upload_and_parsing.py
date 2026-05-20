import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mastering Streamlit - Step 6",
    page_icon="📥",
    layout="centered"
)

st.title("Step 6: File Upload Processing & Dynamic Ingestion")
st.caption("Filenamed: 06_file_upload_and_parsing.py | Target: Accepting user data at runtime")

st.header("1. Data File Ingestion Engine")
st.write("To make your app useful to other people, you must build it to process outside files.")

uploaded_file = st.file_uploader(
    label="Upload your business metrics file (Expects a CSV format)",
    type=["csv"],
    help="Upload a comma-separated values file containing numeric columns for parsing."
)

st.divider()


if uploaded_file is None:
    st.info("💡 **Waiting for User Action:** Please drag and drop a valid CSV file above to populate the data grid.")
    
    # Let's provide a quick snippet of mock CSV code they can copy to make a test file!
    with st.expander("Need a test file? Copy this text into a blank notepad document and save it as 'test.csv'"):
        st.code("""Item,Cost,Units_Sold
Product A,45.50,120
Product B,12.00,450
Product C,89.99,75
Product D,150.00,30
""", language="text")

else:
    # SUCCESS STATE: A file is present in memory. 
    # Streamlit wraps the file in a buffer object. We pass it directly into pd.read_csv()
    try:
        user_dataframe = pd.read_csv(uploaded_file)
        
        st.success(f"🎉 **File Ingested Successfully!** Filename detected: `{uploaded_file.name}`")
        
        # Display the uploaded data structure
        st.subheader("Raw Extracted Data Matrix")
        st.dataframe(user_dataframe, use_container_width=True)
        
        st.divider()
        
        # ==========================================
        # 3. DYNAMIC DATA ANALYSIS & CHART EXTRACTION
        # ==========================================
        st.subheader("Automated Summary Metrics")
        
        # Let's write robust column validation rules. 
        # We look for a categorical text column and numeric metrics columns to draw charts.
        numeric_columns = user_dataframe.select_dtypes(include=['number']).columns.tolist()
        text_columns = user_dataframe.select_dtypes(include=['object']).columns.tolist()
        
        if len(numeric_columns) == 0:
            st.warning("⚠️ The uploaded file does not contain any numeric values. Unable to compute statistical aggregates.")
        else:
            # Let the user interactively choose which numeric column they want to chart!
            target_chart_metric = st.selectbox(
                "Choose a metric to map out visually:", 
                options=numeric_columns
            )
            
            # Create horizontal breakdown layout split into two columns
            col_metric, col_chart = st.columns([1, 2])
            
            with col_metric:
                st.write("📊 **Quick Statistics**")
                max_val = user_dataframe[target_chart_metric].max()
                min_val = user_dataframe[target_chart_metric].min()
                avg_val = user_dataframe[target_chart_metric].mean()
                
                st.metric(label=f"Maximum {target_chart_metric}", value=f"{max_val:,.2f}")
                st.metric(label=f"Minimum {target_chart_metric}", value=f"{min_val:,.2f}")
                st.metric(label=f"Average {target_chart_metric}", value=f"{avg_val:,.2f}")
                
            with col_chart:
                st.write(f"📈 **Visual Spread of {target_chart_metric}**")
                
                # If there is a text column available, let's use it as our chart index categories!
                if text_columns:
                    chart_prep = user_dataframe.set_index(text_columns[0])
                    st.bar_chart(chart_prep[[target_chart_metric]])
                else:
                    st.bar_chart(user_dataframe[[target_chart_metric]])
                    
    except Exception as error_log:
        # If a user uploads a broken file or an incompatible schema, catch the exception cleanly
        st.error(f"🛑 **Critical Parsing Error:** The file data format could not be verified. Technical log: {error_log}")