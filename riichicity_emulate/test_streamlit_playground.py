from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_playground.py")
assert not at.exception
