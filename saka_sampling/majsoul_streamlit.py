import streamlit as st
import majsoul_sanma_sample

# import yonma_sample

st.set_page_config(layout="wide")
st.title("rcity 10dan saka Sampling")

num_games = st.selectbox("Number of games", [100, 500, 1000, 2000, 3000], index=1)
# num_dan = st.selectbox("Number of dan", [7, 8, 9, 10], index=3)
num_max_pt = st.selectbox("Number of max points", [4000, 7000, 10000, 20000], index=3)
# if num_games is None or num_dan is None:
#     st.stop()
df = majsoul_sanma_sample.readcsv()
if df is not None:
    if st.button("再計算") or num_games is not None:
        col1, col2 = st.columns(2)
        plt = majsoul_sanma_sample.simulate_games(df, num_games=num_games, max_score=num_max_pt)
        with col1:
            st.pyplot(plt)
        with col2:
            st.dataframe(df)
