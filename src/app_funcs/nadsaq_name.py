import streamlit as st
import yfinance as yf
from src.Preprocessing import select_columns, change_level, change_type

def load_nasdaq_data():
    name = st.text_input("Enter NASDAQ Symbol of Company")
    data= yf.download(name)
    columns = select_columns.columns_set(data)
    df = change_level.drop_level(data, columns)
    df_ = change_type.change_type(df)
    return df_