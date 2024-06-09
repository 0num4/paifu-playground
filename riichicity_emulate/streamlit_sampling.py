import streamlit as st
import rcity_tenho_sampling
import majsoul_sanma_sample

# import yonma_sample

st.set_page_config(layout="wide")
st.title("tenho or rcity 10dan saka Sampling")

num_games = st.selectbox("Number of games", [100, 500, 1000, 2000, 3000], index=1)
num_dan = st.selectbox("Number of dan", [7, 8, 9, 10], index=3)
platform = st.selectbox("platform", ("rcity", "tenhou", "majsoul"), key="platform")
print(f"platform: {platform}, enum: {rcity_tenho_sampling.Platform[platform]}")
num_max_pt = st.selectbox("Number of max points", [9000, 10000, 15000, 20000], index=3)
col1, col2, col3 = st.columns(3)
with col1:
    custom_1st_p = st.number_input("1st rate(custom)", min_value=0.0, max_value=1.0)
with col2:
    custom_2nd_p = st.number_input("2nd rate(custom)", min_value=0.0, max_value=1.0)
with col3:
    custom_3rd_p = st.number_input("3rd rate(custom)", min_value=0.0, max_value=1.0)
custom_rates = None
if custom_1st_p + custom_2nd_p + custom_3rd_p == 1.0:
    st.info("custom rating enabled")
    custom_rates = [custom_1st_p, custom_2nd_p, custom_3rd_p]
print(f"1st: {custom_1st_p}, 2nd: {custom_2nd_p}, 3rd: {custom_3rd_p}")
if num_games is None or num_dan is None:
    st.stop()
# TODO: この辺の場合分けなんとかしたい
if rcity_tenho_sampling.Platform[platform] == rcity_tenho_sampling.Platform.majsoul:
    st.info("majsoul三麻は段位システムが違うためallでフィルターしています")
    df = majsoul_sanma_sample.readcsv(dan_filter="all")
else:
    df = rcity_tenho_sampling.readcsv(
        filter=num_dan, platform=rcity_tenho_sampling.Platform[platform]
    )
if df is not None:
    if st.button("再計算") or num_games is not None:
        col1, col2 = st.columns(2)
        if (
            rcity_tenho_sampling.Platform[platform]
            == rcity_tenho_sampling.Platform.majsoul
        ):
            plt = majsoul_sanma_sample.simulate_games(
                df, num_games=num_games, max_score=num_max_pt
            )
        else:
            plt = rcity_tenho_sampling.simulate_games(
                df, num_games=num_games, max_score=num_max_pt, custom_rates=custom_rates
            )
        with col1:
            st.pyplot(plt)
        with col2:
            st.dataframe(df)
