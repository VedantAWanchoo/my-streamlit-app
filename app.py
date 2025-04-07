
import streamlit as st

st.title("Hello, Streamlit! 👋")
st.write("This is a simple Streamlit app.")
st.write("Here's a number:", 100)

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

