from statsmodels.graphics.tsaplots import plot_acf
def plot_acf_graph(df_1,col):
  fig = plot_acf(df_1[col].dropna())
  return fig