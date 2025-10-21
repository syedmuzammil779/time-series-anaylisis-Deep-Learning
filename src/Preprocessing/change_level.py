def drop_level(df, cols):
  df_selected = df.loc[:, cols]
  df_selected.columns = df_selected.columns.droplevel(1)  
  df_selected.reset_index(inplace=True)
  return df_selected