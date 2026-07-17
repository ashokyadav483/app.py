import pandas as pd
import os

CSV_FILE = "alarm_database.csv"

if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"{CSV_FILE} not found.")

# Read CSV
df = pd.read_csv(
    CSV_FILE,
    dtype=str,
    encoding="utf-8-sig"
)

# Remove extra spaces
df.columns = df.columns.str.strip()
df = df.apply(lambda x: x.astype(str).str.strip())

print("CSV Loaded Successfully")
print("Columns:", df.columns.tolist())

# Check required columns
required_columns = [
    "AlarmCode",
    "AlarmName",
    "Cause",
    "ElectricalCheck",
    "MechanicalCheck",
    "Solution",
    "SparePart"
]

for col in required_columns:
    if col not in df.columns:
        raise Exception(f"Missing column: {col}")

def search_alarm(code):
    code = str(code).strip()

    result = df[df["AlarmCode"] == code]

    if result.empty:
        return None

    return result.iloc[0]
