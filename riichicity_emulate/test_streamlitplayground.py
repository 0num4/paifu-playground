from streamlit.testing.v1 import AppTest

at = AppTest.from_file("test_streamlitplayground.py")
assert not at.exception
