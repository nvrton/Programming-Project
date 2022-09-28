#from optparse import Values
import PySimpleGUI as sg

class windclass():
    def windmain():
        sg.theme("DarkBrown")
        val = 0

        title_column = [
            [sg.Text("Wind Strength")]

        ]

        button_column = [
            [sg.Button("Done")]
        ]

        layout = [ 
            [sg.Column(title_column)],
            
            [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                        enable_events=True, key="wind"), sg.Text("wind")],
            [sg.Column(button_column, element_justification='right', expand_x=True)]
        ]

        window = sg.Window("Nuclear Reactor Meltdown Simulator", layout, resizable=True, return_keyboard_events=True)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Done":
                global sliderval
                sliderval = values["wind"]
                print(sliderval)
                break

        window.close()
    #windmain()