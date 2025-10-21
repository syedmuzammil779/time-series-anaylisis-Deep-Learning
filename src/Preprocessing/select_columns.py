def columns_set(df):
  select = ["close", "open", "date", "high", "volume"]
  selected_col = []
  for cols in df.columns:
    for col in cols:
      if col.lower() in select:
        selected_col.append(col)
  return selected_col