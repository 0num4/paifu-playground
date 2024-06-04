import streamlit as st
import sample
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Streamlit Sample")

num_games = st.selectbox("Number of games", [100, 500, 1000, 2000, 3000], index=1)
num_dan = st.selectbox("Number of dan", [7, 8, 9, 10], index=3)
if num_games is None or num_dan is None:
    st.stop()
df = sample.readcsv(filter=num_dan)
if df is not None:
    if st.button("再計算") or num_games is not None:
        col1, col2 = st.columns(2)
        plt = sample.simulate_games(df, num_games=num_games)
        with col1:
            st.pyplot(plt)
        with col2:
            st.dataframe(df)
