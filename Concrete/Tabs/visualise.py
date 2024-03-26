"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns


import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise the Concrete Strength Estimatation")

  
    if st.checkbox("Cement Amount vs Strength"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="cement",y="strength",data=df)
        st.pyplot()

    if st.checkbox("Slag Amount vs Strength"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="slag",y="strength",data=df)
        st.pyplot()

    if st.checkbox("Water Amount vs Strength"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="water",y="strength",data=df)
        st.pyplot()

   
