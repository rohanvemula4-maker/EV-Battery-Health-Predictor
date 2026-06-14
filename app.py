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
try:
    with open("battery_health_model.pkl", "rb") as file:
        model = pickle.load(file)

except Exception as e:
    st.error(f"Model Loading Error: {e}")
    st.stop()

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

# Features
st.markdown("""
### Project Features

✅ Machine Learning Based Prediction

✅ Battery Health Assessment

✅ Real-Time Prediction

✅ Interactive Dashboard

✅ EV Battery Analytics
""")

# Sidebar
st.sidebar.header("Battery Parameters")

battery_capacity = st.sidebar.number_input(
    "Battery Capacity (kWh)",
    min_value=0.0,
    value=75.0
)

vehicle_age = st.sidebar.number_input(
    "Vehicle Age (Months)",
    min_value=0,
    value=24
)

charging_cycles = st.sidebar.number_input(
    "Charging Cycles",
    min_value=0,
    value=500
)

temperature = st.sidebar.number_input(
    "Average Temperature (°C)",
    min_value=-20.0,
    value=30.0
)

fast_charge_ratio = st.sidebar.number_input(
    "Fast Charge Ratio",
    min_value=0.0,
    max_value=1.0,
    value=0.5
)

discharge_rate = st.sidebar.number_input(
    "Average Discharge Rate",
    min_value=0.0,
    value=1.0
)

internal_resistance = st.sidebar.number_input(
    "Internal Resistance (Ohm)",
    min_value=0.0,
    value=0.03
)

# Prediction
if st.button("🔋 Predict Battery Health"):

    input_data = pd.DataFrame({
        "Battery_Capacity_kWh": [battery_capacity],
        "Vehicle_Age_Months": [vehicle_age],
        "Total_Charging_Cycles": [charging_cycles],
        "Avg_Temperature_C": [temperature],
        "Fast_Charge_Ratio": [fast_charge_ratio],
        "Avg_Discharge_Rate_C": [discharge_rate],
        "Internal_Resistance_Ohm": [internal_resistance]
    })

    prediction = model.predict(input_data)[0]

    prediction = max(0, min(100, prediction))

    st.metric(
        "Battery Health (SoH)",
        f"{prediction:.2f}%"
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

except Exception as e:
    st.warning(f"Graph Error: {e}")

# Footer
st.markdown("---")

st.caption(
    "Developed by Rohan | EV Battery Health Prediction"
)