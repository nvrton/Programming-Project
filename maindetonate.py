import tkinter 
import customtkinter as ck


class Settings(ck.CTk):
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
