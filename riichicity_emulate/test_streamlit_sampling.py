import streamlit.testing.v1

at = streamlit.testing.v1.AppTest.from_file("streamlit_sampling.py")
at.run(timeout=10)
select = at.selectbox[0]
assert select.options == ["100", "500", "1000", "2000", "3000"]
assert not at.exception
