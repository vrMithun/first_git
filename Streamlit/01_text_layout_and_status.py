import streamlit as st

st.set_page_config(
    page_title="Mastering Streamlit - Step 1",
    page_icon="🚀",
    layout="centered"
)

st.title("Step 1: Advanced Text, Display, & Status Elements")
st.caption("Filenamed: 01_text_layout_and_status.py | Target: Complete typography mastery")

st.header("1. Document Structure & Typography")
st.subheader("Markdown & Text formatting")
st.markdown("""
Streamlit uses Markdown for standard text. This allows you to easily format text:
- **Bold text** using `**text**` or *italics* using `*text*`.
- Create [hyperlinks](https://streamlit.io).
- Add inline code blocks like `variable = 10`.
""")

st.divider()

st.header("2. Technical & Mathematical Displays")
st.subheader("Code Blocks")
st.write("To display code snippets with syntax highlighting without executing them:")
example_python_code = """
def calculate_growth(initial, rate, periods):
    return initial * ((1 + rate) ** periods)
"""
st.code(example_python_code, language="python")
st.subheader("Mathematical LaTeX Expressions")
st.write("Crucial for financial, statistical, or engineering dashboards:")
st.latex(r"A = P \left(1 + \frac{r}{n}\right)^{nt}")
st.divider()

st.header("3. Executive Dashboard Metrics")
st.write("The `st.metric` element is perfect for KPI cards at the top of a dashboard.")

st.metric(
    label="Quarterly Active Users (QAU)", 
    value="14,230 Users", 
    delta="+12.3% vs Last Qtr"
)

st.divider()

st.header("4. Status Messages & User Feedback")
st.write("Dashboards need to tell users if processes succeeded, failed, or need attention.")

st.info("💡 **Tip:** Always group your setup configurations at the very top of your script.")
st.warning("⚠️ **Warning:** Large data frames might slow down rendering times without caching.")
st.error("🛑 **Error:** Unable to connect to the primary data source. Attempting fallback...")
st.success("🎉 **Success:** All database tables loaded and indexed successfully!")