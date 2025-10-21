import plotly.express as px
import pandas as pd
import streamlit as st

def plot_graph(data , col,start_date, end_date, spn = 20,):
    date= []
    for column in data.columns:
      if "date" in column.lower():
        date.append(column)
    data= data[(data[date[0]]>= str(start_date)) & (data[date[0]]<=str(end_date))]
    data = data.reset_index()
    data =  data.set_index(date[0])
    # Ensure the data used is a 1-dimensional Series by squeezing or flattening if necessary.
    y_data = data[col]  # Use squeeze() to remove extra dimensions if present
    # Calculate the Exponential Weighted Moving Average (EWMA)
    y_data_ewma = y_data.ewm(span=spn, adjust=False).mean()

    # Combine original data and EWMA in a DataFrame to plot them together
    plot_data = pd.DataFrame({
        'Original': y_data,
        'EWMA': y_data_ewma
    }, index=data.index)  # Ensure index alignment

    # Plot using Plotly Express
    fig = px.line(plot_data, title=f'{col} Stock Price Over Time')
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text=col, range=[min(y_data) * 0.95, max(y_data) * 1.05])

    # Show the plot
    return fig