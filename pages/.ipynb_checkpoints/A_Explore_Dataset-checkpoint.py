from collections import UserString
import streamlit as st                  
import pandas as pd
import plotly.express as px

#############################################

st.markdown("# Practical Applications of Machine Learning (PAML)")

#############################################

st.markdown("### Homework 0 - Introduction to Streamlit")

#############################################

st.markdown('# Explore Dataset')

###################### FETCH DATASET #######################

uploaded_file = st.file_uploader("Upload your CSV data", type="csv")
data = pd.read_csv(UserString/liuzeyan/Documents/GitHub/homework0/datasets/housing_paml.csv)
st.session_state['data'] = load_data(uploaded_file)

###################### EXPLORE DATASET #######################

# Restore dataset if already in memory

# Display feature names and descriptions 

# Display dataframe as table

#X = df

###################### VISUALIZE DATASET #######################

# Collect user plot selection

# Specify Input Parameters

# Plot Histogram