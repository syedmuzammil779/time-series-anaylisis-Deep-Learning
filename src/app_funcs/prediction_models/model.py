import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import streamlit as st

def train_sarimax_predict(data, target_col, p, d, q, P, D, Q, s=12, forecast_steps=4):
    """
    Train a SARIMAX model and forecast future values.

    Parameters:
    - data (pd.DataFrame): The input time series data.
    - target_col (str): The column name of the target variable in the DataFrame.
    - p, d, q (int): ARIMA orders.
    - P, D, Q (int): Seasonal orders.
    - s (int): Seasonal period.
    - forecast_steps (int): Number of steps to forecast.

    Returns:
    - results.summary(): SARIMAX model summary.
    - predictions (pd.Series): Predicted values for the forecast steps.
    """
    try:

        # Ensure the target column exists in the data
        if target_col not in data.columns:
            st.write("1")
            raise ValueError(f"Column '{target_col}' not found in the dataset.")


        # Extract the target time series
        time_series = data[target_col]

        # Fit the SARIMAX model
        model = SARIMAX(
            time_series,
            order=(p, d, q),
            seasonal_order=(P, D, Q, s),
            enforce_stationarity=False,
            enforce_invertibility=False
        )
        results = model.fit(disp=False)

        # Forecast future values
        predictions = results.forecast(steps=forecast_steps)

        # Return the model summary and predictions
        st.write(data)
        return results.summary(), predictions

    except Exception as e:
        st.write("An error Occured")
        return str(e), None


