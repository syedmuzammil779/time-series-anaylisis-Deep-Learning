import streamlit as st

import pandas as pd
from Tools.scripts.pindent import start


def integer_column_selector(df):
    date= []
    for cols in df.columns:
        if "date" in cols.lower():
            date.append(cols)
            break
    int_columns = df.select_dtypes(include=['int', 'float']).columns.tolist()

    if not int_columns:
        st.sidebar.write("No integer columns available.")
        return None
    col1, col2 ,col3= st.columns((1,2,2))
    df[date[0]] = pd.to_datetime(df[date[0]], errors='coerce')
    with col1:
        col = st.selectbox("Select", options=int_columns)
    with col2:
        start_date = st.date_input(
            "Start Date",
            min_value=df[date[0]].dt.date.min(),
            value=df[date[0]].dt.date.min(),
            key="start_date"  # Add a unique key for streamlit caching
        )


    with col3:
        end_date = st.date_input(
            "End Date",
            max_value=df[date[0]].dt.date.max(),
            key="end_date"  # Add a unique key for streamlit caching
        )

    return col, start_date, end_date
