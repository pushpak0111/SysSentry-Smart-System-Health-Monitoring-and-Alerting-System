# ---------------------------
# Import dependencies
# ---------------------------
import pandas as pd
import streamlit as st
import plotly.express as px
import os

# ---------------------------
# Streamlit page configuration
# ---------------------------
st.set_page_config(page_title="SysSentry Dashboard", layout="wide")

# Page title displayed at top
st.title("🖥️ SysSentry: System Monitoring Dashboard")

# File paths for metrics and alerts
metrics_file = "data/metrics.csv"
alerts_file = "data/alerts.csv"

# ---------------------------
# Function to load metrics data
# Cached = faster reloads (Streamlit cache)
# ---------------------------
@st.cache_data
def load_metrics():
    if os.path.exists(metrics_file):
        return pd.read_csv(metrics_file)
    else:
        return pd.DataFrame()  # Empty DataFrame if file missing

# ---------------------------
# Function to load alerts data
# ---------------------------
@st.cache_data
def load_alerts():
    if os.path.exists(alerts_file):
        return pd.read_csv(alerts_file)
    else:
        return pd.DataFrame()

# Load data into DataFrames
df = load_metrics()

# ---------------------------
# Display Metrics Chart
# ---------------------------
if df.empty:
    st.warning("⚠️ No data available yet! Run monitor.py to start logging metrics.")
else:
    st.subheader("📊 System Metrics Overview")

    # Create line chart using Plotly
    fig = px.line(
        df, 
        x="timestamp", 
        y=["cpu_percent", "memory_percent", "disk_percent"],
        labels={"value": "Usage (%)", "variable": "Metric"},
        title="System Resource Usage Over Time"
    )

    # Display chart
    st.plotly_chart(fig, width='stretch')

    # ---------------------------
    # Display Latest System Readings
    # ---------------------------
    st.subheader("🟢 Latest System Readings")
    latest = df.iloc[-1]

    # st.metric creates small visual boxes with key data
    st.metric("CPU Usage (%)", f"{latest['cpu_percent']:.2f}")
    st.metric("Memory Usage (%)", f"{latest['memory_percent']:.2f}")
    st.metric("Disk Usage (%)", f"{latest['disk_percent']:.2f}")

# ---------------------------
# Display Recent Alerts Section (Enhanced with Diagnostics)
# ---------------------------
from diagnostics import suggest_fix  # ✅ Import suggestion function

alerts_df = load_alerts()
st.subheader("⚠️ Recent Alerts Log with Suggestions")

if alerts_df.empty:
    st.success("✅ No alerts recorded yet. System running smoothly.")
else:
    # Create a new column in DataFrame with suggested fixes
    alerts_df["Suggested Fix"] = alerts_df["alert"].apply(suggest_fix)
    
    # Show only last 10 alerts for readability
    st.dataframe(alerts_df.tail(10))
