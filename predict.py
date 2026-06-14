import pickle
import pandas as pd

# Load model
with open("models/battery_model.pkl", "rb") as file:
    model = pickle.load(file)

# New battery data
new_battery = pd.DataFrame({
    "Charge_Cycles": [850],
    "Voltage": [3.4],
    "Temperature": [38],
    "Capacity": [81]
})

# Predict
prediction = model.predict(new_battery)

print(f"Predicted Battery Health: {prediction[0]:.2f}%")