import pandas as pd

def change_type(df):
  select = ["close", "open", "high", "volume"]
  for col in df.columns:
    if col.lower() in select:
      df[col] = df[col].astype("float64")
    elif "date" in col.lower() :
      df[col] = pd.to_datetime(df[col])
  return df