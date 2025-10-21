from statsmodels.tsa.stattools import adfuller


# Function to perform the Dickey-Fuller test and return results
def dickey_fuller_test(df_selected, col):
    # Ensure the series is not constant after dropping NaNs
    data = df_selected[col].dropna()
    # if data.max() == data.min():
    #     print("Series is constant. Cannot perform Dickey-Fuller test.")
    #     return True  # Assume stationary to exit the loop in make_data_stationary

    result = adfuller(data)

    # # Output ADF Statistic and p-value
    # print(f'ADF Statistic: {result[0]:.6f}')
    # print(f'p-value: {result[1]:.6f}')
    # print('Critical Values:')
    # for key, value in result[4].items():
    #     print(f'\t{key}: {value:.3f}')

    # Return True if the series is stationary (p-value <= 0.05)
    return result[1] <= 0.05