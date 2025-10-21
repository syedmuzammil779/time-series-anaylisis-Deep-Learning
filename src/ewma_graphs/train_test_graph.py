import matplotlib.pyplot as plt
def plot_train_test_split(df_selected, col):
  fig= plt.figure(figsize=(10, 6))
  plt.plot(df_selected[col], label='Original Data')
  plt.axvline(df_selected.index[int(len(df_selected) * 0.8)], color='r', linestyle='--',
              label='Train-Test Split')
  plt.title("Train and Test Ratio")
  return fig


