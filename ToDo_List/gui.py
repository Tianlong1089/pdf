import functions
import PySimpleGUI as sg

label = sg. Text("Type in a to-do")
input_box =  sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

list_box = sg.Listbox(values = functions.get_todos(), key = 'todos',enable_events=True, size=[45,10] )

window = sg.Window('My To-Do App', layout= [[label], [input_box,add_button],[list_box,edit_button, complete_button],[exit_button]],font = ('Helvetica',20))

while True:
        event, values = window.read()
        #print(1,values)
        #print(2,values['todos'])
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
                    print("new :", new_todo)
                    print("todo_to_edit " ,todo_to_edit)


                    todos=functions.get_todos()
                    print("Todos: ", todos)
                    index = todos.index(todo_to_edit)

                    todos[index]= new_todo

                    print(todos)
                    functions.write_todos(todos)

                    window['todos'].update(values=todos)

                except IndexError:
                    print('Choose a option while editing')
                    continue
            case 'Complete':
                todo_complete = values['todos'][0]
                print("todo_to_edit ", todo_complete)
                todos = functions.get_todos()
                index = todos. index(todo_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            case "Exit":
                break
            case 'todos':
                window['todo'].update(value=values['todos'][0])
            case sg.WINDOW_CLOSED:
                break

window.close()



