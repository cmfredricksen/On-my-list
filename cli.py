# from functions import get_todos, write_todos
import functions as functions
import time

while True:
    now = time.strftime("%b %d, %Y at %H:%M %p")
    print(f"It is {now}")
    user_action = input("Type in add, show(s), edit, complete or exit(x): ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("s"):
        todos = functions.get_todos()

        for i, item in enumerate(todos):
            item = item.strip("\n") 
            row = f"[{i + 1}]   {item.title()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Please enter changes:  ") + "\n"
            todos[number] = new_todo

            
            functions.write_todos(todos)

        except ValueError:
            print("You must enter the number of the task you want to edit.")
            continue

    elif user_action.startswith("complete"):            
        try:

            todos = functions.get_todos()

            number = int(user_action[9:])
            
            index = number -1
            completed_todo = todos[index].strip('\n')
            message = f"Todo {completed_todo.upper()} has been marked complete."
            todos.pop(index)

            functions.write_todos(todos)

            print(message)

        except ValueError:
            print("You must enter the number of the TODO that is completed.")
            continue

        except IndexError:
            print("There is no item with that number.")
            continue

    elif 'exit' in user_action or 'x' in user_action:
        break

    else:
        print("Command is not recognized, try again.")


print("You have exited the todo list")