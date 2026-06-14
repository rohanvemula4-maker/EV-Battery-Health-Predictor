import streamlit as st
import pandas as pd
import pickle

# Page Configuration
st.set_page_config(
    page_title="EV Battery Health Predictor",
    page_icon="🔋",
    layout="wide"
)

# Load Model
with open("models/battery_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🔋 EV Battery Health Predictor")

st.markdown("""
Predict the State of Health (SoH) of an Electric Vehicle Battery using Machine Learning.
""")

# Dashboard Cards
col1, col2 = st.columns(2)

with col1:
    st.metric("Model Accuracy", "98.61%")

with col2:
    st.metric("Dataset Size", "10,000 Records")

# Features Section
st.markdown("""
### Project Features

✅ Machine Learning Based Prediction

✅ Battery Health Assessment

✅ Real-Time Prediction

✅ Interactive Dashboard

✅ EV Battery Analytics
""")

# Sidebar Inputs
st.sidebar.header("Battery Parameters")

charge_cycles = st.sidebar.number_input(
    "Charge Cycles",
    min_value=0,
    value=500
)

voltage = st.sidebar.number_input(
    "Voltage (V)",
    min_value=0.0,
    value=400.0
)

temperature = st.sidebar.number_input(
    "Temperature (°C)",
    min_value=-20.0,
    value=30.0
)

capacity = st.sidebar.number_input(
    "Capacity (kWh)",
    min_value=0.0,
    value=75.0
)

# Prediction
if st.button("🔋 Predict Battery Health"):

    input_data = pd.DataFrame({
        "Charge_Cycles": [charge_cycles],
        "Voltage": [voltage],
        "Temperature": [temperature],
        "Capacity": [capacity]
    })

    prediction = model.predict(input_data)[0]

    # Keep prediction between 0 and 100
    prediction = max(0, min(100, prediction))

    st.metric(
        "Battery Health (SoH)",
        f"{prediction:.1f}%"
    )

    st.progress(prediction / 100)

    if prediction >= 90:
        st.success("✅ Excellent Battery Condition")

    elif prediction >= 80:
        st.success("✅ Healthy Battery")

    elif prediction >= 60:
        st.warning("⚠ Moderate Degradation")

    else:
        st.error("❌ Battery Replacement Recommended")

# Graph Section
# Graph Section
st.subheader("📊 Battery Analysis Graphs")

try:

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "images/soh_vs_cycles.png",
            caption="Battery Health vs Charging Cycles",
            use_container_width=True
        )

        st.image(
            "images/temperature_vs_soh.png",
            caption="Temperature vs Battery Health",
            use_container_width=True
        )

    with col2:
        st.image(
            "images/resistance_vs_soh.png",
            caption="Resistance vs Battery Health",
            use_container_width=True
        )

except:
    st.info("Graphs not found.")

# Footer
st.markdown("---")

st.caption(
    "Developed by Rohan | EV Battery Health Prediction"
)