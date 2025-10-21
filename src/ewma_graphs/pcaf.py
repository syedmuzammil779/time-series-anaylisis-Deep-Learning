# import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import  plot_pacf
def plot_pacf_graph(df_1, col):
    fig = plot_pacf(df_1[col].dropna())
    return fig