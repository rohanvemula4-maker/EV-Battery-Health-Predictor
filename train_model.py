import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv(
    "data/clean_battery_dataset.csv"
)
X = data[
    [
        "Battery_Capacity_kWh",
        "Vehicle_Age_Months",
        "Total_Charging_Cycles",
        "Avg_Temperature_C",
        "Fast_Charge_Ratio",
        "Avg_Discharge_Rate_C",
        "Internal_Resistance_Ohm"
    ]
]
y = data["SoH_Percent"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
lr = LinearRegression()

lr.fit(
    X_train,
    y_train
)

lr_score = lr.score(
    X_test,
    y_test
)

print(
    "Linear Regression Accuracy:",
    lr_score
)
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(
    X_train,
    y_train
)
rf_score = rf.score(
    X_test,
    y_test
)

print(
    "Random Forest Accuracy:",
    rf_score
)
if rf_score > lr_score:
    print("Random Forest Selected")
else:
    print("Linear Regression Selected")

with open(
    "battery_health_model.pkl",
    "wb"
) as file:

    pickle.dump(
        rf,
        file
    )

print("Model Saved Successfully")    