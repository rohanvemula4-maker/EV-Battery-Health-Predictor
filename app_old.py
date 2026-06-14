import streamlit as st
import pickle
import pandas as pd

# Load model
with open("models/battery_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("EV Battery Health Predictor")

st.write("Enter battery details below:")

charge_cycles = st.number_input("Charge Cycles", min_value=0, value=800)
voltage = st.number_input("Voltage", min_value=0.0, value=3.5)
temperature = st.number_input("Temperature (°C)", value=35)
capacity = st.number_input("Capacity (%)", min_value=0, value=80)

if st.button("Predict Battery Health"):

    battery_data = pd.DataFrame({
        "Charge_Cycles": [charge_cycles],
        "Voltage": [voltage],
        "Temperature": [temperature],
        "Capacity": [capacity]
    })

    prediction = model.predict(battery_data)

    st.success(f"Predicted Battery Health: {prediction[0]:.2f}%")