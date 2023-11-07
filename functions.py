text_file = 'todos.txt'


def get_todos(filepath=text_file):
    """Reads a text file and returns a list
    of todo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def save_todos(todos_in, filepath=text_file):
    """Writes files to replace todos in a text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_in)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
