import PySimpleGUI as sg
from FeetToMeters import feet_to_meters
from FeetToMeters import inches_to_meters

sg.theme("SystemDefaultForReal")

label1 = sg.Text("Enter Feet:")
input1 = sg.Input(key="feets")

label2 = sg.Text("Enter Inches:")
input2 = sg.Input(key="inches")

convertor_button = sg.Button("Convert")
label3 = sg.Text(key = 'amount')
exit_button = sg.Button("Exit")

window = sg.Window("Convertor", layout = [[label1,input1],[label2,input2],[convertor_button,exit_button, label3]])
while True:
    event,values=window.read()

    match event:
        case "Convert":
            feets=float(values['feets'])
            inches=float(values['inches'])
            meters =  feet_to_meters(feets) + inches_to_meters(inches)
            string = f'{meters} m'
            window['amount'].update(value= string)
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()