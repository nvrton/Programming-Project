import tkinter 
import customtkinter as ck
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


class Settings(ck.CTk):#haven't figured out customtkinter setup config yet, so am still using pysimplegui code, once i figure this out i will swap over main.py to call settings 
    WIDTH = 480
    HEIGHT = 580

    def __init__(self):
        super().__init__()

        self.title("Settings")
        self.geometry(f"{Settings.WIDTH}x{Settings.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.closing)

        
        self.grid_columnconfigure(1, weight=1)#exact specifics behind how this works I do not know, mostly done through trial and error.
        self.grid_rowconfigure(1, weight=1)#removing this blocks off the bottom half of the window so it stays
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #self.frame_left = ck.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)#both sections here set up the layout of
        #self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")#the two columns I have made. along with giving them a name

        #self.frame_right = ck.CTkFrame(master=self, corner_radius=0)
        #self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        #this builds the left hand frame

        self.frame_1 = ck.CTkFrame(master=self, corner_radius=0)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)
        
        self.frame_1.grid_rowconfigure(4, weight=1)#sets up the number of rows in my left frame

        

        

        def slider1_event(value):
            print(int(value))

        slider1 = ck.CTkSlider(master=self, from_=0, to=100, command=slider1_event)
        slider1.grid(padx=0.5, pady=0.5, row=0, column=0)

        def slider2_event(value):
            print(int(value))

        slider2 = ck.CTkSlider(master=self, from_=0, to=100, command=slider2_event)
        slider2.grid(padx=0.5, pady=0.5, row=1, colum=0)

        def slider3_event(value):
            print(int(value))

        slider3 = ck.CTkSlider(master=self, from_=0, to=100, command=slider3_event)
        slider3.grid(padx=0.5, pady=0.5, row=2, colum=0)

        def slider4_event(value):
            print(int(value))

        slider4 = ck.CTkSlider(master=self, from_=0, to=100, command=slider4_event)
        slider4.grid(padx=0.5, pady=0.5, row=3, colum=0)

    

    def closing(self):
        self.destroy()

if __name__ == "__main__":
    settings = Settings()
    settings.mainloop()
