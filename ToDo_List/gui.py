import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass

sg.theme('SystemDefaultForReal')

clock = sg.Text('',key='clock')
label = sg. Text("Type in a to-do")
input_box =  sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

list_box = sg.Listbox(values = functions.get_todos(), key = 'todos',enable_events=True, size=[45,10] )

window = sg.Window('My To-Do App', layout= [[clock],[label], [input_box,add_button],[list_box,edit_button, complete_button],[exit_button]],font = ('Helvetica',20))

while True:
        event, values = window.read(timeout=100)
        window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
        match event:
            case "Add":
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            case "Edit":
                try:
                    todo_to_edit = values['todos'][0]
                    if todo_to_edit[-2:] == '\n':
                        new_todo = values['todo']
                    else:
                        new_todo = values['todo'] + '\n'
                    if todo_to_edit[-4:] == '\n\n':
                        new_todo = new_todo[:-2]
                    #print("new :", new_todo)
                    #print("todo_to_edit " ,todo_to_edit)


                    todos=functions.get_todos()
                    #print("Todos: ", todos)
                    index = todos.index(todo_to_edit)

                    todos[index]= new_todo

                    #print(todos)
                    functions.write_todos(todos)

                    window['todos'].update(values=todos)

                except IndexError:
                    sg.popup('Please choose a option while editing.',font=("Helvatica",20))
                    continue
            case 'Complete':
                try:
                    todo_complete = values['todos'][0]
                    #print("todo_to_edit ", todo_complete)
                    todos = functions.get_todos()
                    index = todos. index(todo_complete)
                    todos.pop(index)
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
                except IndexError:
                    sg.popup("Please, select the todo completed. ", font=("Helvatica",20))
            case "Exit":
                break
            case 'todos':
                window['todo'].update(value=values['todos'][0])
            case sg.WINDOW_CLOSED:
                break

window.close()



