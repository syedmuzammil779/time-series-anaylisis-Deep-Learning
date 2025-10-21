from src.app_funcs import data_uploader, menu, metrice, nadsaq_name
import streamlit as st
from src.ewma_graphs import graphs , pcaf,acf
from src.app_funcs.sidebar import side_menue
from src.app_funcs.prediction_menue import menue_prediction_page
from src.ewma_graphs.acf import plot_acf_graph
from src.ewma_graphs.pcaf import plot_pacf_graph
from src.ewma_graphs.train_test_graph import plot_train_test_split
from src.app_funcs.prediction_models import check_stationary, model

def load_css(css_file_path):
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize df in session state if not already present
if 'df' not in st.session_state:
    st.session_state.df = None

opt = side_menue.side_m()
st.title("Time Series Analysis")
method = st.selectbox("Method", options=["Upload a File", "By Name"])

# Check if df is already stored, otherwise load based on user choice
try:
    if st.session_state.df is None:
        if method == "Upload a File":
            st.session_state.df = data_uploader.dataset_from_user()
        elif method == "By Name":
            st.session_state.df = nadsaq_name.load_nasdaq_data()
except:
    st.write("Please Enter Nadsaq Name")
if opt:
    try:


        # Use the persisted df for further processing if it's available
        if st.session_state.df is not None:
            df = st.session_state.df
            st.write("----")
            load_css("css/style.css")
            metrice.metric(df)
            cols, start_date, end_date = menu.integer_column_selector(df)
            fig = graphs.plot_graph(df, col=cols, start_date=start_date, end_date=end_date)
            st.plotly_chart(fig)
    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    df = st.session_state.df
    st.title("Prediction")
    p, d, q, P, D, Q= menue_prediction_page()

    target = []
    for col_ in df.columns:
        if "close" in col_.lower():
            target.append((col_))
    val = check_stationary.dickey_fuller_test(df, target)
    if val:
        st.write("<p style='color:red;'>Data is Stationary</p>", unsafe_allow_html=True)
    else:
        st.write("<p style='color:red;'>Data is not Stationary</p>", unsafe_allow_html=True)
    fig = plot_train_test_split(df, target)
    st.pyplot(fig)
    col1, col2 = st.columns(2)
    with col1:
        fig = plot_pacf_graph(df, target)
        st.pyplot(fig)
    with col2:
        fig= plot_acf_graph(df, target)
        st.pyplot(fig)
    _ , prediction = model.train_sarimax_predict(df, target, p, d, q, P, D, Q)
    st.write(prediction)



