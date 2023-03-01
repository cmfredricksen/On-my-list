import streamlit as st
import functions

todos = functions.get_todos()

st.title("On my list...")
st.subheader("Keeping up with life.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add a todo:", placeholder="Add a todo...", label_visibility="hidden")

