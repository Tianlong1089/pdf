FilePath  = 'todos.txt'
def get_todos(pathfile=FilePath):
  """REad a text file and return the list of to-do items."""
  with open(pathfile,'r') as file_local:
    todos_local= file_local.readlines()
  return todos_local

def write_todos(todos_loc,path_file=FilePath):
  """ Write the to-do items list in the text file."""
  with open(path_file,'w') as file:
    file.writelines(todos_loc)

if __name__ == '__main__':
  print("Function Ready !!")