import streamlit as st
from api import get_multiple_jokes

st.title("😂 Multi Joke App")

num = st.number_input("How many jokes?", min_value=1, step=1)

if st.button("Get Jokes"):
    jokes = get_multiple_jokes(num)

for joke in jokes:
    if "error" in joke:
        st.error(joke["error"])
    else:
        st.info(joke["type"])
        st.write(joke["setup"])
        st.success(joke["punchline"])