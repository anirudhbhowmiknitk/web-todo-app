import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()

    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)

    st.session_state["new_todo"] = ""


st.title("🚀 My Todo App")
st.subheader("Manage your tasks efficiently")

# Add new task
st.text_input(
    "",
    placeholder="Add a new task...",
    key="new_todo",
    on_change=add_todo
)

st.divider()

for index, todo in enumerate(todos):

    col1, col2, col3 = st.columns([6, 2, 2])

    # Task text
    with col1:
        completed = st.checkbox(
            todo.strip(),
            key=f"complete_{index}"
        )

    # Edit button
    with col2:
        if st.button("✏️", key=f"edit_btn_{index}"):

            edited = st.text_input(
                "Edit Task",
                value=todo.strip(),
                key=f"edit_input_{index}"
            )

            if st.button("Save", key=f"save_{index}"):

                todos[index] = edited + "\n"

                functions.write_todos(todos)

                st.rerun()

    # Delete button
    with col3:
        if st.button("🗑️", key=f"delete_{index}"):

            todos.pop(index)

            functions.write_todos(todos)

            st.rerun()

    # Complete checkbox removes task
    if completed:

        todos.pop(index)

        functions.write_todos(todos)

        st.rerun()