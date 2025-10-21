import streamlit as st
import pandas as pd
import os
import zipfile
import io

# Title of the web app

def dataset_from_user():
    df= None
    st.header("Stock Data Upload")
# File uploader for multiple files
    uploaded_files = st.file_uploader("Upload your stock data files", type=['csv', 'xlsx'], accept_multiple_files=True)

    if uploaded_files:
        dataframes = {}
        for uploaded_file in uploaded_files:
            # Read the uploaded file into a DataFrame
            if uploaded_file.name.endswith('csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                st.error(f"Unsupported file format: {uploaded_file.name}")
                continue

            # Store the DataFrame in a dictionary using the file name as the key
            dataframes[uploaded_file.name] = df

        # Display the names of the uploaded files and a preview of the data
        st.write("Uploaded Data Files:")
        for filename, df in dataframes.items():
            st.write(f"**{filename}**")
        return df


