import PySimpleGUI as sg 


layout = [[sg.Text("Hello World")], [sg.Button("OK")], [sg.calendar()]]


window = sg.Window("Demo", layout, margins=(500, 200))

while True:
    event, values = window.read()
    if event =="OK" or event == sg.WIN_CLOSED:
        break

window.close()  