import pandas as pd

data = pd.read_csv("data/clean_battery_dataset.csv")

print("\nFIRST 10 ROWS")
print(data.head(10))

print("\nCOLUMN NAMES")
print(data.columns.tolist())

print("\nDATASET INFO")
print(data.info())