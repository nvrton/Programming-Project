import tkinter
import customtkinter as ck
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return False
    except:
        return True


def connect_window():
    if connect():

            def button_callback():
                app.destroy()
                connect_window()

            ck.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
            ck.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

            app = ck.CTk()
            app.geometry("400x150")
            app.title("Error!")

            frame_1 = ck.CTkFrame(master=app)
            frame_1.pack(pady=20, padx=60, fill="both", expand=True)

            label_1 = ck.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Please connect to the internet")
            label_1.pack(pady=12, padx=10)

            button_1 = ck.CTkButton(master=frame_1, text=("Try Again"), command=button_callback)
            button_1.pack(pady=12, padx=10)

            

            app.mainloop()
            return False
    else:  
        print("Connected!")
        return True 
