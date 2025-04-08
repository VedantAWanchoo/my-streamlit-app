
import streamlit as st

st.title("Hello, User! 👋")
st.write("This is my first Streamlit app.")


name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

