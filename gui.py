import PySimpleGUI as sg
import functions as functions
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkBlue4")

# PYGUI widgets, add to layout below
clock = sg.Text("Date:  ", key="clock", font=("courier", 14))
label = sg.Text("Enter a todo: ")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("add", tooltip="Add new todo", key="add")

list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])

edit_button = sg.Button("edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")

# In the layout, each list is equal to one row
layout = [
    [clock],
    [label], 
    [input_box, add_button], 
    [list_box, edit_button, complete_button],
    [exit_button]
    ]

window = sg.Window("On my List...", layout, font=("helvetica", 16))

while True:
    event, values = window.read() # after this point, mutate data and return response, finish by closing
    window["clock"].update(value=time.strftime("%A, %b %d, %Y"))
    # print(f"Event: {event}")
    # print(f"Values: {values}")
    match event:
        case 'add':
            todos = functions.get_todos()

            new_todo = values["todo"] + "\n"
            todos.append(new_todo)

            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        
        case 'edit':
            try:    
                todo_edit = values["todos"][0]
                new_todo = values["todo"] 

                todos = functions.get_todos()

                index = todos.index(todo_edit)
                todos[index] = new_todo + "\n"

                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            
            except IndexError:
                sg.popup("Please select a todo from the list first.", font=("Helvetica", 14))

            except ValueError:
                sg.popup("Value Error")

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'complete':
            try:
                todo_complete = values["todos"][0]

                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")

            except IndexError:
                sg.popup("Please select a todo from the list first.", font=("Helvetica", 14))

            except ValueError:
                sg.popup("Value Error")

        case 'exit':
            break

        case sg.WIN_CLOSED:
            break


window.close()


