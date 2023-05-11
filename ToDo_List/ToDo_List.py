import time
import functions


now = time.strftime("%b %d, %Y %H:%M:%S")
todos = []
while True:
    user_action = input(' Type add, show, edit, complete or exit: \n')
    user_action = user_action.strip()
    if user_action.startswith('add'):  # add case
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):  # show case

        todos = functions.get_todos()

        todos = [palabra.strip('\n') for palabra in todos]
        for index, item in enumerate(todos):
            row = f'{index + 1}:{item}'
            print(row)

    elif user_action.startswith('edit'):  # edit case
        todos = functions.get_todos()
        print(f'These are the activities saved : {todos} \n')

        number = int(input('Enter the number of todo to edit: '))
        number = number - 1

        print('Got it!  ', number + 1)

        new_todo = input('Enter new todo \n')
        todos[number] = new_todo + '\n'

        functions.write_todos(todos)

    elif user_action.startswith('complete'):  #
        try:
            todos = functions.get_todos()
            print(todos)

            number = int(input("Number complete: \n"))
            print(f'This todo was removed {todos[number - 1]} okay!')
            todos.pop(number - 1)

            functions.write_todos(todos)

        except IndexError:
            print(f"There is no item with number {number}.  Try again. ")
            continue

    elif user_action == 'exit':
        break

    else:
        print('Command is not valid. Please type [edit / show /complete /exit] ')
print('Bye')