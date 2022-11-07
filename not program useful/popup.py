import tkinter
import customtkinter


class ExampleApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        self.button = customtkinter.CTkButton(self, text="Create Toplevel", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)

    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)


app = ExampleApp()
app.mainloop()