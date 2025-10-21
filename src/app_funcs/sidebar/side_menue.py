import streamlit as st
def side_m():
    model =st.sidebar.selectbox("Select Page", options= ["Time Series", "Prediction Model"])
    if model=="Time Series":
        return True
    return False
