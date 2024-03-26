import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache_data()
def load_data():

    df = pd.read_csv('asphalt.csv')

    # Perform feature and target split
    X = df[["Water_Cement_Ratio","Standing_Time","Aggregate_Quality","Asphalt_Quantity","Fly_Ash_Content","Stone_Chips_Percent","Sand_Ratio","Temperature_Range","Other_Factors"]]
    y = df['Result']

    return df, X, y

@st.cache_data()
def train_model(X, y):
    # Create the model
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1, 
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42, splitter='best'
        )
    model.fit(X, y)
    score = model.score(X, y)
    return model, score

def predict(X, y, features):
    model, score = train_model(X, y)
    
    prediction = model.predict(np.array(features).reshape(1, -1))
    return prediction, score