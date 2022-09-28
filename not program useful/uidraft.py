import PySimpleGUI as sg



def windows():
    sg.theme("DarkBrown")
    map_view_column= [
        [sg.Text("Insert Map Here")],
        [sg.In(size=(25, 1), enable_events=True, key="-MAP SPOT-")],
    ]

    info_column = [
        [sg.Text("Info about stuff and options")],
        [sg.In(size=(25, 1), enable_events=True, key="-INFO SPOT-")],
    ]



    layout = [
        [sg.Column(map_view_column),
        sg.VSeperator(),
        sg.Column(info_column),
        sg.Button("Click me"),]
    ]

    layout2 = [
        [sg.Text("Hello bro"),
        sg.Button("nice")]
    ]


    window = sg.Window("Nuclear Reactor Meltdown Simulator", layout, resizable=True)
    window2= sg.Window("Part two baby", layout2, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Click me":
            text = values["-MAP SPOT-"]
            print(text)
            window.close()#closes original window
            event, values = window2.read()#opens second window
            if event == sg.WIN_CLOSED or event == "nice":
                break

    window.close()

windows()

    #this works finally. event, values is only way it works, not sure what values does. 

    #cannot have window.close() in while loop, must break in if then jump to window.close()


