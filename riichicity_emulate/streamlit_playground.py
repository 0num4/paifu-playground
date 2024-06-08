import streamlit as st

st.title("Hello, world!")
n = st.selectbox("Select a number", [1, 2, 3], index=1, key="selectbox")
print(n)
st.write("n is", n)

