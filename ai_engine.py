import pandas as pd

# Read CSV
df = pd.read_csv(
    "alarm_database.csv",
    dtype=str,
    encoding="utf-8-sig"
)

# Clean column names
df.columns = df.columns.str.strip()

# Clean data
df = df.apply(lambda col: col.astype(str).str.strip())


def search_alarm(code):
    code = str(code).strip()

    result = df[df["AlarmCode"] == code]

    if result.empty:
        return None

    return result.iloc[0]
