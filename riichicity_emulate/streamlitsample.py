import streamlit as st
import sample
import matplotlib.pyplot as plt

st.title("Streamlit Sample")

df = sample.readcsv()
if df is not None:
    st.pyplot(sample.simulate_games(df, num_games=2000, initial_score=3800))
