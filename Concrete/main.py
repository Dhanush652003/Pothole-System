import streamlit as st
from web_functions import load_data
from Tabs import home, data, predict, visualise
st.set_page_config(
    page_title = 'Concrete Strength Estimation',
    page_icon = '🏗️',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

Tabs = {
    "Home": home,
    "Data Info": data,
    "Estimation": predict,
    "Visualisation": visualise
}
st.sidebar.title("Navigation")

page = st.sidebar.radio("Pages", list(Tabs.keys()))
df, X, y = load_data()

if page in ["Estimation", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
