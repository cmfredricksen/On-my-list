import PySimpleGUI as sg
import modules.functions as functions

# PYGUI widgets, add to layout below
label = sg.Text("Add todo")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("add")

show_button = sg.Button("show")
edit_button = sg.Button("edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")
button_box = [[add_button], [show_button], [edit_button], [complete_button], [exit_button]]

# In the layout, each list is equal to one row
layout = [[label], [input_box, add_button], [show_button, edit_button, complete_button], [exit_button]]

window = sg.Window("On my List...", layout)

event, values = window.read() # after this point, mutate data and return response, finish by closing

if event == "add":
    print("The event was add")
elif event == "show":
    print("It's time to see the list")
elif event == "edit":
    print("Something else edit!")
elif event == "complete":
    print(f"{event} is complete")
elif event == "exit":
    print("You shall exit...")

print(f"{values[0].upper()} is on my list")
print(event)

window.close()

