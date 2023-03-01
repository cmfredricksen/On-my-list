import streamlit as st
import functions

todos = functions.get_todos()
placeholder_text = "Add a todo..."

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = placeholder_text


st.title("On my list...")
st.subheader("Keeping up with life.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        

st.text_input(label="Add a todo:", placeholder=placeholder_text, label_visibility="hidden", on_change=add_todo, key="new_todo")



