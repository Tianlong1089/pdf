import PySimpleGUI as sg
from zip_extractor import unzip

sg.theme('SystemDefaultForReal')

label_file = sg.Text("Select zip")
input = sg.Input()
file_button = sg.FilesBrowse("Choose", key="file")

label_folder = sg.Text("Select folder")
input1 =sg.Input()
folder_button = sg.FolderBrowse("Choose",key="folder")

extract_button = sg.Button("Extract")
label_done = sg.Text(key='done',text_color="green")

window = sg.Window('Archive Extractor',layout=[[label_file,input,file_button],[label_folder,input1,folder_button],[extract_button,label_done]])


while True:
    events, values = window.read()
    match events:
         case 'Extract':
            try:
                path_file = values['file']
                folder_path = values['folder']
                unzip(path_file,folder_path)
                window['done'].update(value="File extracted !!!")

            except FileNotFoundError:
                sg.popup('Please, select a file.', font=('Arial', 15))
         case sg.WINDOW_CLOSED:
            break

window.close()


