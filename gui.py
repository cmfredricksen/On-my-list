import PySimpleGUI as sg
import modules.functions as functions

# PYGUI widgets, add to layout below
label = sg.Text("Add todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("add")


# In the layout, each list is equal to one row
layout = [
    [label], 
    [input_box, add_button], 
    ]

window = sg.Window("On my List...", layout, font=("helvetica", 16))

while True:
    event, values = window.read() # after this point, mutate data and return response, finish by closing
    print(event)
    print(values)
    match event:
        case 'add':
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            print(f"{new_todo.upper()} was added to my list...")

        case sg.WIN_CLOSED:
            break



window.close()


