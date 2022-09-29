#from sqlite3 import SQLITE_DROP_VTABLE
import customtkinter as ck
from tkinter import *
from tkcalendar import Calendar
from tkintermapview import TkinterMapView
from maindetonate import detonation
from tkinter import CENTER
import math
#from smartlearning import Smartlearning
#test123
### MAP CREDIT:    https://github.com/TomSchimansky/TkinterMapView ###
### tkinter used for UI ###
##  where do i put damageradius = smartlearning.predict(text) ??

class Map(ck.CTk):#defines the class map - to be used later
    APP_NAME = "Nuclear Reactor Meltdown Simulator" #name of
    WIDTH = 900 #dimensions
    HEIGHT = 600

    def set_marker_event(self):#
        self.clear_marker_event()
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))
        print(current_position)
        
    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def detonate_event(self):
        def polygon_click(polygon):
            print(f"polygon clicked - text: {polygon.name}")

        #switzerland_marker = self.map_widget.set_address("Switzerland", marker=True, text="Switzerland")
        #self.map_widget.set_zoom(8)

        detonateposition = self.map_widget.get_position()
        print(detonateposition)
        detonateposition = str(detonateposition)

        latitude,longitude = detonateposition.split(",")
        latitude = latitude.strip("(")
        longitude = longitude.strip(")")
        latitude = float(latitude)
        longitude = float(longitude)
        print(latitude)
        print(longitude)
        point1La = (latitude)
        point1Lo = (longitude-0.4407)
        point2La = (latitude+0.2701)
        point2Lo = (longitude)
        point3La = (latitude)  
        point3Lo = (longitude+0.4407)
        point4La = (latitude-0.2701)
        point4Lo = (longitude)
        testpointLa = (latitude+1.135)
        testpointLo = (longitude-1.2205)
        

        self.map_widget.set_polygon([(point1La,point1Lo),
                                     
                                     (point2La,point2Lo),
                                     (point3La,point3Lo),
                                     (point4La,point4Lo)],
                                            # fill_color=None,
                                            # outline_color="red",
                                            # border_width=12, 
                                            command=polygon_click,
                                            name="detonation_polygon")
        detonation.main()

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

    def wind_choose_event(self):
        root = Tk()

        root.title("Select Wind Strength")
        root.geometry("200x200")

        slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
        slider.set(0)

        slider.pack(pady = 20)

        def grad_date():
            global windchoice
            wind.config(text = "Selected Wind Strength is: " + str(slider.get()))
            windchoice = str(slider.get())
            print(windchoice)
            self.windtext = ck.CTkLabel(self.frame_left, text=windchoice, anchor="center")
            self.windtext.grid(padx=(20, 20), pady=(20, 0), row=4, column=0,)

        Button(root, text = "Set Wind Strength", command = grad_date).pack(pady = 20)
            
        wind = Label(root, text = "")
        wind.pack(pady = 20)

        root.mainloop()

    def date_choose_event(self):
        root = Tk()

        root.title("Choose the date")
        root.geometry("400x400")

        cal = Calendar(root, selectmode = 'day', year = 2022, month = 9, day = 14)

        cal.pack(pady = 20)

        def grad_date():
            global datechoice
            date.config(text = "Selected Date is: " + cal.get_date())
            datechoice = cal.get_date()
            print(datechoice)
            self.datetext = ck.CTkLabel(self.frame_left, text=datechoice, anchor="center")
            self.datetext.grid(padx=(20, 20), pady=(20, 0), row=2, column=0,)

        Button(root, text = "Get Date", command = grad_date).pack(pady = 20)
            
        date = Label(root, text = "")
        date.pack(pady = 20)

        root.mainloop()
    
    def __init__(self, *args, **kwargs):#defines main bulk of setup code, where everything is defined
        super().__init__(*args, **kwargs)#passes any positional and keyword arguments to the parent (I'm thinking being class()?)

        self.title(Map.APP_NAME)#sets title of program to APP_NAME - predefined
        self.geometry(str(Map.WIDTH) + "x" + str(Map.HEIGHT))#sets launch dimensions as whatever I defined them as above
        self.minsize(Map.WIDTH, Map.HEIGHT)#sets the minimum size of the program to whatever the launch dimensions are

        self.marker_list=[]

        self.protocol("WM_DELETE_WINDOW", self.on_closing)#this clears the window should I close it
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)#quits something upon closing of the program

        #creating the two sections to my program, two sides on the window,
        #one side will have the map, one side will have the information (eventually)
        #known as frames in tkinter module 

        self.grid_columnconfigure(1, weight=0)#these define the size of the frames relative to eachother
        self.grid_columnconfigure(1, weight=1)#exact specifics behind how this works I do not know, mostly done through trial and error.
        self.grid_rowconfigure(0, weight=1)#removing this blocks off the bottom half of the window so it stays

        self.frame_left = ck.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)#both sections here set up the layout of
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")#the two columns I have made. along with giving them a name

        self.frame_right = ck.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        #this builds the left hand frame

        
        self.frame_left.grid_rowconfigure(8, weight=1)#sets up the number of rows in my left frame

        self.button_1 = ck.CTkButton(master=self.frame_left,#creates a button
                                                text="Set Marker",#calls it set marker
                                                command=self.set_marker_event)#this is the event i use in if statments to make it do stuff
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row = 0, column = 0)#this sets up location of button 
        

        self.button_2 = ck.CTkButton(master=self.frame_left,
                                                text="Detonate",
                                                command=self.detonate_event)
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=5, column=0)

        self.datechoose = ck.CTkButton(master=self.frame_left,
                                                text="Choose Date",
                                                command=self.date_choose_event)
        self.datechoose.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

        datechoice = "No Date Selected"
        self.datetext = ck.CTkLabel(self.frame_left,
                                                text=datechoice, 
                                                anchor="center")
        self.datetext.grid(padx=(20, 20), pady=(20, 0), row=2, column=0)

        
        self.windchoose = ck.CTkButton(master=self.frame_left,
                                                text="Wind Strength",
                                                command=self.wind_choose_event)
        self.windchoose.grid(pady=(20,0), padx=(20, 20), row=3, column=0)

        windchoice = "No Wind Selected"
        self.windtext = ck.CTkLabel(self.frame_left,
                                                text=windchoice, 
                                                anchor="center")
        self.windtext.grid(padx=(20, 20), pady=(20, 0), row=4, column=0)

        def optionmenu_callback(choice):
                print("optionmenu dropdown clicked:", choice)
        self.combobox = ck.CTkOptionMenu(master=self.frame_left,
                                                    values=["Chernobyl", "option 2"],
                                                    command=optionmenu_callback)
        self.combobox.grid(padx=(20, 20), pady=(10, 0), row=6, column=0)

        

        #this builds the right hand frame

        self.frame_right.grid_rowconfigure(1, weight=1)#sets up the grid the right hand frame operates in
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)#sets up the map widget :D
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.map_widget.set_address("Solihull")#sets address to start on to cheltenham
        #self.map_option_menu.set("OpenStreetMap")#sets the map to street view (rather than satelight)
        #self.appearance_mode_optionemenu.set("Dark")#sets map to dark mode rather than light mode

if __name__ == "__main__":
    map = Map()
    map.start()
