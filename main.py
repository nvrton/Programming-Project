#from sqlite3 import SQLITE_DROP_VTABLE
import customtkinter as ck
from tkinter import *
from tkcalendar import Calendar
from tkintermapview import TkinterMapView
from maindetonate import detonation
from tkinter import CENTER
from internetping import *
#from smartlearning import Smartlearning

### MAP CREDIT:    https://github.com/TomSchimansky/TkinterMapView ###
### tkinter used for UI ###
## where do i put damageradius = smartlearning.predict(text) ?? ##
## rememebr to add: reset(removes all radius of damage), delete secondary window if another loads?, ##

class Map(ck.CTk):# defines the class map 
    APP_NAME = "Nuclear Reactor Meltdown Simulator" # name of
    WIDTH = 900 # dimensions
    HEIGHT = 600


    def set_marker_event(self, coords):
        self.clear_marker()# deletes any existing marker
        current_position = self.map_widget.get_position()# sets current position to centre of map (dynamic variable, takes middle whenever new marker made)
        self.marker_list.append(self.map_widget.set_marker(coords[0], coords[1]))# adds a marker to array with coordinates of centre of screen 
        self.marker_position = (coords[0], coords[1])# creates new fixed variable of said marker position 
        print(self.marker_position)

    #def set_polygon_marker(self):
        #middle_point = self.marker_position# using fixed variable from above, plots marker here for polygon centre 
        #self.polygon_marker_list.append(self.map_widget.set_marker(middle_point[0], middle_point[1]))


    def clear_marker(self):
        for marker in self.marker_list:
            marker.delete()


    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()
        for self.polygon1 in self.polygon_list:
            self.polygon1.delete()
        for marker in self.polygon_marker_list:
            marker.delete()


    def userchoice(self, choice):
        global reactorchoice# choice is not a variable I cannot manipulate, only read, so must be set to one I can manipulate, hence, reactorchoice.
        reactorchoice = choice
        

    def sella(self): 
        latitude = 54.420494091731996
        longitude = -3.499754145054311
        longstraight = 0.1177935
        latstraight = 0.0721811
        longsmall = 0.08507753813
        latsmall = 0.05213821774

        point1La = (latitude)
        point1Lo = (longitude-longstraight)
        point2La = (latitude+latsmall)
        point2Lo = (longitude-longsmall)
        point3La = (latitude+latstraight)
        point3Lo = (longitude)
        point4La = (latitude+latsmall)  
        point4Lo = (longitude+longsmall)
        point5La = (latitude)
        point5Lo = (longitude+longstraight)
        point6La = (latitude-latsmall)
        point6Lo = (longitude+longsmall)
        point7La = (latitude-latstraight)
        point7Lo = (longitude)
        point8La = (latitude-latsmall)
        point8Lo = (longitude-longsmall)

        self.polygon1 = self.map_widget.set_polygon([(point1La,point1Lo),
                                    (point2La,point2Lo),
                                    (point3La,point3Lo),
                                    (point4La,point4Lo),
                                    (point5La,point5Lo),
                                    (point6La,point6Lo),
                                    (point7La,point7Lo),
                                    (point8La,point8Lo)],
                                            # fill_color=None,
                                            # outline_color="red",
                                            # border_width=12, 
                                            name="detonation_polygon")
        self.polygon_list.append(self.polygon1)

    def set_polygon_marker(self):
        try:
            middle_point = self.marker_position# using fixed variable from above, plots marker here for polygon centre 
            if reactorchoice == "Sellafield Reactor":
                self.polygon_marker_list.append(self.map_widget.set_marker(middle_point[0], middle_point[1], text="Sellafield Reactor"))
            elif reactorchoice == "Chernobyl":
                self.polygon_marker_list.append(self.map_widget.set_marker(middle_point[0], middle_point[1], text="Chernobyl"))
            elif reactorchoice == "Three Mile Island":
                self.polygon_marker_list.append(self.map_widget.set_marker(middle_point[0], middle_point[1], text="Three Mile Island"))
            elif reactorchoice == "Fukushima-Daiichi":
                self.polygon_marker_list.append(self.map_widget.set_marker(middle_point[0], middle_point[1], text="Fukushima-Daiichi"))
        except:
            self.polygon_marker_list.append(self.map_widget.set_marker(middle_point[0], middle_point[1], text="Sellafield Reactor"))
 
    def create_toplevel(self):
        window = ck.CTkToplevel(self)
        window.geometry("270x200")
        window.title("Error!")

        # create label on CTkToplevel window
        label = ck.CTkLabel(window, text="Please select a marker position!")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=20)
        
        button = ck.CTkButton(window, text="Close", command=window.destroy)
        button.pack(side="bottom", fill="both", expand=True, padx=40, pady=30)

    def detonate_event(self):
        try:
            if reactorchoice == "Sellafield Reactor":
                print("Sellafield Reactor")
                longstraight = 0.1177935
                latstraight = 0.0721811
                longsmall = 0.08507753813
                latsmall = 0.05213821774
            elif reactorchoice == "Chernobyl":
                print("Chernobyl")
                longstraight = 0.4407
                latstraight = 0.2701
                longsmall = 0.3183
                latsmall = 0.1951
            elif reactorchoice == "Three Mile Island":
                print("Three Mile Island")
                longstraight = 0.4739935
                latstraight = 0.290384
                longsmall = 0.3423465647
                latsmall = 0.2097516416
            elif reactorchoice == "Fukushima-Daiichi":
                print("Fukushima-Daiichi")
                longstraight = 0.5924935
                latstraight = 0.3659811
                longsmall = 0.4279343795
                latsmall = 0.2643573218
        except:# if reactorchoice is not filled, it set values to Sellafield Reactor
            self.combobox.set("Sellafield Reactor")
            print("Sellafield Reactor")
            longstraight = 0.1177935
            latstraight = 0.0721811
            longsmall = 0.08507753813
            latsmall = 0.05213821774 

        def polygon_click(polygon):
            print(f"polygon clicked - text: {polygon.name}")

        try:
            detonateposition = self.marker_position# uses fixed variable to put it where marker was, not centre of screen 
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
            point1Lo = (longitude-longstraight)
            point2La = (latitude+latsmall)
            point2Lo = (longitude-longsmall)
            point3La = (latitude+latstraight)
            point3Lo = (longitude)
            point4La = (latitude+latsmall)  
            point4Lo = (longitude+longsmall)
            point5La = (latitude)
            point5Lo = (longitude+longstraight)
            point6La = (latitude-latsmall)
            point6Lo = (longitude+longsmall)
            point7La = (latitude-latstraight)
            point7Lo = (longitude)
            point8La = (latitude-latsmall)
            point8Lo = (longitude-longsmall)
            
            self.set_polygon_marker()

            global polygon1
            self.polygon1 = self.map_widget.set_polygon([(point1La,point1Lo),
                                        (point2La,point2Lo),
                                        (point3La,point3Lo),
                                        (point4La,point4Lo),
                                        (point5La,point5Lo),
                                        (point6La,point6Lo),
                                        (point7La,point7Lo),
                                        (point8La,point8Lo)],
                                                # fill_color=None,
                                                # outline_color="red",
                                                # border_width=12, 
                                                command=polygon_click,
                                                name="detonation_polygon")
            self.polygon_list.append(self.polygon1)
        except:
            print("No marker placed")
            self.create_toplevel()


    def on_closing(self, event=0):
        self.destroy()


    def start(self):
        self.mainloop()


    def wind_choose_event(self):
        
        window = ck.CTkToplevel(self)
        window.geometry("290x200")
        window.title("Select Wind Strength")

        # create label on CTkToplevel window
        slider = ck.CTkSlider(window, from_=0, to=100, orient="horizontal", command=window.update())
        slider.set(0)
        slider.pack(side="top", expand=True, padx=40, pady=20)
        
        def set_wind():
            global windchoice
            #wind.config(text = "Selected Wind Strength is: " + str(slider.get()))
            windchoice = int(slider.get())
            windchoice = str(windchoice)
            print(windchoice)
            windchoice = (windchoice, "mph North")
            self.windtext = ck.CTkLabel(self.frame_left, text=windchoice, anchor="center")
            self.windtext.grid(padx=(20, 20), pady=(20, 0), row=3, column=0,)
            window.destroy()
        
        button = ck.CTkButton(window, text="Set Wind Strenth", command=set_wind)
        button.pack(side="bottom", fill="both", expand=True, padx=40, pady=30)

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
            self.datetext.grid(padx=(20, 20), pady=(20, 0), row=1, column=0,)

        Button(root, text = "Get Date", command = grad_date).pack(pady = 20)
            
        date = Label(root, text = "")
        date.pack(pady = 20)

        root.mainloop()
    

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google Normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        elif new_map == "Google Satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())


    def __init__(self, *args, **kwargs):# defines main bulk of setup code, where everything is defined
        super().__init__(*args, **kwargs)# passes any positional and keyword arguments to the parent (I'm thinking being class()?)

        ##TITLE AND SIZE##
        self.title(Map.APP_NAME)# sets title of program to APP_NAME - predefined
        self.geometry(str(Map.WIDTH) + "x" + str(Map.HEIGHT))# sets launch dimensions as whatever I defined them as above
        self.minsize(Map.WIDTH, Map.HEIGHT)# sets the minimum size of the program to whatever the launch dimensions are

        ##ARRAYS FOR OVERLAYS##
        self.marker_list=[]
        self.polygon_list=[]
        self.polygon_marker_list=[]

        ##CLOSING SYSTEM##
        self.protocol("WM_DELETE_WINDOW", self.on_closing)# this clears the window should I close it
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)# quits something upon closing of the program

        ##SETS 2X1 LAYOUT, TWO COLLUMNS, ONE ROW OF ENTIRE WINDOW##
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ##LEFT FRAME SETUP##
        self.frame_left = ck.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)# both sections here set up the layout of
        self.frame_left.grid(row=0, column=0, sticky="nsew")# the two columns I have made. along with giving them a name 

        ##RIGHT FRAME LAYOUT##
        self.frame_right = ck.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, sticky="nsew")

        ##LEFT FRAME GAPS, TO PUT RESET AT BOTTOM#
        self.frame_left.grid_rowconfigure(7, weight=1)# creates gap
        #self.frame_left.grid_rowconfigure(8, minsize=20)# empty row with minsize as spacing
        #self.frame_left.grid_rowconfigure(9, minsize=10)# empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10) 

        ##LEFT HAND FRAME OPTIONS## 
        self.datechoose = ck.CTkButton(master=self.frame_left,# creates a button
                                                  text="Choose Date",# sets button text to Set Marker
                                                  command=self.date_choose_event)# sets command for button
        self.datechoose.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)# this sets up location of button 

        datechoice = "No Date Selected"
        self.datetext = ck.CTkLabel(self.frame_left,
                                        text=datechoice, 
                                        anchor="center")
        self.datetext.grid(padx=(20, 20), pady=(20, 0), row=1, column=0)

        self.windchoose = ck.CTkButton(master=self.frame_left,
                                                  text="Wind Strength",
                                                  command=self.wind_choose_event)
        self.windchoose.grid(pady=(20,0), padx=(20, 20), row=2, column=0)

        windchoice = "No Wind Selected"
        self.windtext = ck.CTkLabel(self.frame_left,
                                        text=windchoice, 
                                        anchor="center")
        self.windtext.grid(padx=(20, 20), pady=(20, 0), row=3, column=0)

        combobox_var = ck.StringVar(value="None")
        self.combobox = ck.CTkOptionMenu(master=self.frame_left,
                                                    values=["Sellafield Reactor",  "Chernobyl", "Three Mile Island", "Fukushima-Daiichi"],
                                                    command=self.userchoice,
                                                    variable=combobox_var)
        self.combobox.grid(padx=(20, 20), pady=(10, 0), row=4, column=0)

        self.button_2 = ck.CTkButton(master=self.frame_left,
                                                text="Detonate",
                                                command=self.detonate_event)
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=5, column=0)

        self.map_label = ck.CTkLabel(self.frame_left, text="Map Type:", anchor="w")
        self.map_label.grid(padx=(20, 20), pady=(20, 0), row=8, column=0, )
        self.map_option_menu = ck.CTkOptionMenu(self.frame_left, values=["OS Map", "Google Normal", "Google Satellite"],
                                                                       command=self.change_map)
        self.map_option_menu.grid(padx=(20, 20), pady=(10, 0), row=9, column=0)

        self.reset_button = ck.CTkButton(master=self.frame_left,
                                                    text="Reset",
                                                    command=self.clear_marker_event)
        self.reset_button.grid(pady=(20, 0), padx=(20, 20), row=10, column=0)

        ##RIGHT HAND FRAME LAYOUT##
        ##3X2 THREE COLLUMNS TWO ROWS##
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        

        ##INSERTING MAP##
        self.map_widget = TkinterMapView(self.frame_right, 
                                            corner_radius=0)# sets up the map widget :D
        self.map_widget.grid(row=1, rowspan=2, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))
        self.map_widget.set_address("Solihull")#sets address to start on to solihull./-[]
        # self.map_option_menu.set("OpenStreetMap")#sets the map to street view (rather than satelight)
        # self.appearance_mode_optionemenu.set("Dark")#sets map to dark mode rather than light mode

        self.map_widget.add_left_click_map_command(self.set_marker_event)

       

        self.marker_1 = self.map_widget.set_marker(54.420494091731996, -3.499754145054311, text="Sellafield Site", command=self.sella)
        self.marker_2 = self.map_widget.set_marker(51.389550623435255, 30.099772380175068, text="Chernobyl")
        self.marker_3 = self.map_widget.set_marker(40.15312060549065, -76.72382538884362, text="Three Mile Island")
        self.marker_4 = self.map_widget.set_marker(37.42098526127145, 141.03135070602593, text="Fukushima-Daiichi")
        latitude = 51.389550623435255
        longitude = 30.099772380175068
        longstraight = 0.4407
        latstraight = 0.2701
        longsmall = 0.3183
        latsmall = 0.1951
        point1La = (latitude)
        point1Lo = (longitude-longstraight)
        point2La = ((latitude+latsmall)+0.01706341863953)
        point2Lo = ((longitude-longsmall)-0.087890625)
        point3La = (55.871463005571265)
        point3Lo = (longitude)
        point4La = (51.600317879729694)  
        point4Lo = (30.50623550445897)
        point5La = (latitude)
        point5Lo = (longitude+longstraight)
        point6La = (latitude-latsmall)
        point6Lo = (longitude+longsmall)
        point7La = (latitude-latstraight)
        point7Lo = (longitude)
        point8La = (latitude-latsmall)
        point8Lo = (longitude-longsmall)
        self.polygon_2 = self.map_widget.set_polygon([(point1La,point1Lo),
                                        (point2La,point2Lo),
                                        (point3La,point3Lo),
                                        (point4La,point4Lo),
                                        (point5La,point5Lo),
                                        (point6La,point6Lo),
                                        (point7La,point7Lo),
                                        (point8La,point8Lo)],
                                                # fill_color=None,
                                                # outline_color="red",
                                                # border_width=12, 
                                                name="detonation_polygon")

        self.entry = ck.CTkEntry(master=self.frame_right,
                                            placeholder_text="Search")
        self.entry.grid(row=3, column=0, columnspan=2, sticky="we", padx=(12, 0), pady=12)
        self.entry.entry.bind("<Return>", self.search_event)

        self.button_5 = ck.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=3, column=2, sticky="w", padx=(12, 0), pady=12)


def start():  
    if __name__ == "__main__":
        if connect_window():# runs internet ping check
            map = Map()
            map.start()
        else: 
            start()# if not connected, re runs function
start()
        
