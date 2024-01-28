import streamlit as st
import pandas as pd

#############################################

st.markdown("# Practical Applications of Machine Learning (PAML)")

#############################################

st.markdown("### Homework 0 - Introduction to Streamlit")

#############################################

st.markdown('# Preprocess Dataset')

def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df
    else:
        st.warning("Please upload a CSV file.")

def display_dataframe(df):
    if df is not None:
        st.markdown("### Dataset Features")
        st.dataframe(df)
    else:
        st.error("No dataset available to display.")

def summarize_missing_values(df):
    missing_values = df.isna().sum()
    num_categories_with_missing = missing_values[missing_values > 0].count()
    avg_missing_per_category = missing_values.mean()
    total_missing = missing_values.sum()
    
    summary = f"""
    - Number of Categories with Missing Values: {num_categories_with_missing}
    - Average Number of Missing Values per Category: {avg_missing_per_category:.2f}
    - Total Number of Missing Values: {total_missing}
    """
    st.markdown("### Summary of Missing Values")
    st.markdown(summary)

def display_descriptive_statistics(df, features, stats):
    statistics = df[features].agg(stats)
    st.write(statistics.round(2))

def main():
    st.title("Data Preprocessing App")

    # Step 2: File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if 'df' not in st.session_state or uploaded_file is not None:
        load_data(uploaded_file)

    # Display dataframe
    if 'df' in st.session_state:
        display_dataframe(st.session_state['df'])

        # Step 4: Summarize missing values
        summarize_missing_values(st.session_state['df'])

        # Step 5: Summarize descriptive statistics
        st.markdown("### Descriptive Statistics")
        numeric_columns = list(st.session_state['df'].select_dtypes(['float', 'int']).columns)
        selected_features = st.multiselect("Select Features", numeric_columns)
        stats_options = ['mean', 'median', 'max', 'min']
        selected_stats = st.multiselect("Select Statistics", stats_options)

        if selected_features and selected_stats:
            display_descriptive_statistics(st.session_state['df'], selected_features, selected_stats)

if __name__ == "__main__":
    main()

# I use Chatgpt to figure out how to use state_session to finish this assignment.