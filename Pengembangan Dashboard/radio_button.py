import streamlit as st


genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comendy','Drama', 'Action'),
    horizontal=False
)