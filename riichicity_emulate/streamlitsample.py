import streamlit as st
import sample
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Streamlit Sample")

num_games = st.selectbox("Number of games", [100, 500, 1000, 2000, 3000])
df = sample.readcsv()
if df is not None:
    if st.button("再計算") or num_games is not None:
        col1, col2 = st.columns(2)
        plt = sample.simulate_games(df, num_games=num_games, initial_score=3800)
        with col1:
            st.pyplot(plt)
        with col2:
            st.dataframe(df)
