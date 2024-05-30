import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def testSum(a, b):
    return int(a) + int(b)

ip_input = st.text_input("IP Address to brute force")
a = st.text_input("1st num")
b = st.text_input("2nd num")




st.write("Target IP address is", testSum(a, b))
