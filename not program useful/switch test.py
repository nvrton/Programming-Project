import customtkinter
from tkinter import *
import customtkinter as ck



switch_var = customtkinter.StringVar(value="on")


def switch_event():
    print("switch toggled, current value:", switch_var.get())

toggle_button = Button(text="OFF", width=10, command=switch_event)
toggle_button.pack(pady=10)


switch_1 = customtkinter.CTkSwitch(master=root_tk, text="CTkSwitch", command=switch_event,
                                   variable=switch_var, onvalue="on", offvalue="off")
switch_1.pack(padx=20, pady=10)