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


def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df  # Store the dataframe in session state
    else:
        st.warning("Please upload a CSV file.")

def display_dataframe(df):
    if df is not None:
        st.markdown("### Dataset Features")
        st.write(df.info())
        st.markdown("### Dataset Preview")
        st.dataframe(df)
    else:
        st.error("No dataset available to display.")

def create_histogram(df, feature):
    fig = px.histogram(df, x=feature, title=f'Histogram of {feature}')
    st.plotly_chart(fig)

def main():
    st.title("Data Exploration App")

    # Step 2: File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if 'df' not in st.session_state or uploaded_file is not None:
        load_data(uploaded_file)

    # Display dataframe
    if 'df' in st.session_state:
        display_dataframe(st.session_state['df'])

        # Step 5: Visualize features in histogram chart
        st.sidebar.header("Create Histogram Plot")
        st.sidebar.header("Specify Input Parameters")
        numeric_columns = list(st.session_state['df'].select_dtypes(['float', 'int']).columns)
        selected_feature = st.sidebar.selectbox("Select Feature for Histogram", numeric_columns)
        
        create_histogram(st.session_state['df'], selected_feature)

if __name__ == "__main__":
    main()

