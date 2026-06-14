import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv(
    "data/clean_battery_dataset.csv"
)

# Create images folder automatically
os.makedirs("images", exist_ok=True)

# Graph 1
plt.figure(figsize=(8,5))

plt.scatter(
    data["Total_Charging_Cycles"],
    data["SoH_Percent"]
)

plt.xlabel("Total Charging Cycles")
plt.ylabel("SoH Percent")
plt.title("Battery Health vs Charging Cycles")

plt.savefig(
    "images/soh_vs_cycles.png"
)

plt.close()

# Graph 2
plt.figure(figsize=(8,5))

plt.scatter(
    data["Avg_Temperature_C"],
    data["SoH_Percent"]
)

plt.xlabel("Average Temperature")
plt.ylabel("SoH Percent")
plt.title("Temperature vs Battery Health")

plt.savefig(
    "images/temperature_vs_soh.png"
)

plt.close()

# Graph 3
plt.figure(figsize=(8,5))

plt.scatter(
    data["Internal_Resistance_Ohm"],
    data["SoH_Percent"]
)

plt.xlabel("Internal Resistance")
plt.ylabel("SoH Percent")
plt.title("Resistance vs Battery Health")

plt.savefig(
    "images/resistance_vs_soh.png"
)

plt.close()

print("Graphs generated successfully!")