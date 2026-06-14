import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data/battery_data.csv")

# Features
X = data[["Charge_Cycles", "Voltage", "Temperature", "Capacity"]]

# Target
y = data["Health"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("models/battery_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully!")
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score*100:.2f}%")