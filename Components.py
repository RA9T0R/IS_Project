import streamlit as st
import pandas as pd
 
st.write("""
# This is a Test Components in Streamlit
Hello *world!*
""")
 
number = st.slider("Pick a number", 0, 100)
color = st.color_picker("Pick a color")
file = st.file_uploader("Pick a file")

pets = ["cat", "dog", "fish"]
pet = st.radio("Pick a pet", pets)
date = st.date_input("Pick a date")