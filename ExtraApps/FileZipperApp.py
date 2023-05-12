'''
This program uses GUI (Graphical User Interface)
This Program opens a window to select the file or files to compress, extract the path file and finally
make you choose the path were the zipped file will be created.
'''
import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select destination folder: " )
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",key='folder')

label3= sg.Text("Introduce Zipped Name: ")
input3 = sg.Input(key='name_compressed')

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

window = sg.Window("File Compressor",layout=[[label1,input1,choose_button1],[label2,input2,choose_button2],[label3,input3],[compress_button,output_label]])
while True:
    event, values = window.read()
    match event:
        case 'Compress':
            if ';' in values['files']:
                filepaths = values['files'].split(';')
                print(filepaths)
            else:
                print(values)
                filepaths = values['files']
            folder = values["folder"]
            name = values["name_compressed"]
            print(name)
            make_archive(filepaths,folder,name)

            window["output"].update(value="Compression completed !!!")

        case sg.WINDOW_CLOSED:
            break

window.close()
