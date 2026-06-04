import os

FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass

    with open(file_path, "r") as file:
        todos_local = file.readlines()

    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    with open(file_path, "w") as file:
        file.writelines(todos_arg)