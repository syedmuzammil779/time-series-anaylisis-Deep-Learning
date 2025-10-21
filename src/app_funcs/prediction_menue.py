import streamlit as st


def menue_prediction_page():
    st.header("Enter Hyper Parameters")
    col1, col2, col3= st.columns(3)
    with col1:
        p = st.number_input("Enter p value", min_value=0, max_value=5)
    with col2:

        i = st.number_input("Enter i value")
    with col3:
        q = st.number_input("Enter q value", min_value=0, max_value=5)

    col1, col2, col3 = st.columns(3)
    with col1:
        P = st.number_input("Enter P value", min_value=0, max_value=5)
    with col2:
        I = st.number_input("Enter I value")
    with col3:
        Q = st.number_input("Enter Q value", min_value=0, max_value=5)

    return p,i,q, P,I,Q

