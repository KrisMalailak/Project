import pandas as pd
import streamlit as st


df = pd.DataFrame({
    'c1' : [1, 2, 3, 4],
    'c2' : [10, 20, 30, 40],
})


st.table(data=df)