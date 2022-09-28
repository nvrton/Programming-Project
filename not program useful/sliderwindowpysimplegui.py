import PySimpleGUI as sg

class detonation():
    def main():
        sg.theme("DarkBrown")
        map_view_column= [
            [sg.Text("Insert Map Here")],
            [sg.In(size=(25, 1), enable_events=True, key="-MAP SPOT-")],
        ]

        info_column = [
            [sg.Text("Info about stuff and options")],
            [sg.In(size=(25, 1), enable_events=True, key="-INFO SPOT-")],
        ]

        val = 0

        layout = [
            [sg.Column(map_view_column),
            sg.VSeperator(),
            sg.Column(info_column),
            sg.Button("Click me")],
            [sg.Text("Slider1")],
            [[sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                        enable_events=True, key="slider1"), sg.Text("Slider1")],
            [sg.Text("Slider2")],
            [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                        enable_events=True, key="slider2"), sg.Text("Slider2")],
            [sg.Text("Slider3")],
            [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                        enable_events=True, key="slider3"), sg.Text("Slider3")],
            [sg.Text("Slider4")],
            [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                        enable_events=True, key="slider4"), sg.Text("Slider4")]]
        ]

        layout2 = [
            [sg.Text("Hello bro"),
            sg.Button("nice")]
        ]

    
        #windows = sg.Window("slider test", layouts, return_keyboard_events=True)
        #window.Finalize()

        window = sg.Window("Nuclear Reactor Meltdown Simulator", layout, resizable=True, return_keyboard_events=True)
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
                if event == sg.WIN_CLOSED:
                    break
                elif event == "nice":
                    window.close()
                    window2.close()
                    map.start()

        window.close()

    #main()
    

    #this works finally. event, values is only way it works, not sure what values does. 

    #cannot have window.close() in while loop, must break in if then jump to window.close()
