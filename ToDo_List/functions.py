FilePath  = '/home/tianlong55/Downloads/PyCharm_Projects/ToDo_List/todos.txt'
def get_todos(pathfile=FilePath):
  with open(pathfile,'r') as file_local:
    todos_local= file_local.readlines()
  return todos_local

def write_todos(todos_loc,path_file=FilePath):
  with open(path_file,'w') as file:
    file.writelines(todos_loc)

if __name__ == '__main__':
  print("Function Ready !!")