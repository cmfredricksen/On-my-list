FILEPATH = "files/todos.txt"

def get_todos(file_path=FILEPATH):
    '''Reads the file and returns a list of todos'''
    with open(file_path, 'r') as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, file_path=FILEPATH):
    '''Writes a list of todos to text file'''
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)


