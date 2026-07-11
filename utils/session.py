import streamlit as st

def initialize_session():
    """
    Initialize session state variables.
    """
    if "df" not in st.session_state:
        st.session_state.df = None

def set_dataset(df):
    """
    Store dataframe globally.
    """
    st.session_state.df = df

def get_dataset():
    """
    Retrieve dataframe.
    """
    return st.session_state.df


def clear_dataset():
    """
    Remove dataframe from session.
    """
    st.session_state.df = None

def update_dataset(df):
    """
    Replace the current dataset.
    """
    st.session_state.df = df