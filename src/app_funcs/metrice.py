import streamlit as st
def metric(df):
    st.title("Stock Data Metrics")
    cols = []
    for col in df.columns:
        if "close" in col.lower():
            if col not in cols:

                cols.append(col)
        elif "volume" in col.lower():
            if col not in cols:
                cols.append(col)



    # Calculate latest price, previous close, and volume
    latest_price = df[cols[0]].iloc[-1]  # Latest closing price
    previous_price = df[cols[0]].iloc[-2]  # Previous closing price
    volume = df[cols[1]].iloc[-1]  # Latest volume

    # Calculate percentage change
    percentage_change = ((latest_price - previous_price) / previous_price) * 100
    col1, col2, col3, col4=  st.columns((3,2 ,1, 2))
    with col1:
    # Display metrics
        st.metric(label="Latest Price", value=f"${latest_price:.2f}")
    with col2:
        st.metric(label="Percentage Change", value=f"{percentage_change:.2f}%", delta=f"{percentage_change:.2f}%")
    with col4:

        st.metric(label="Volume", value=int(volume))