import customtkinter

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkOptionMenu(master=app,
                                       values=["option 1", "option 2"],
                                       command=optionmenu_callback)
combobox.pack(padx=20, pady=10)
#combobox.set("option 2")  # set initial value