import tkinter as tk 
# from tkinter import ttk
import ttkbootstrap as ttk

def convert () :
    mile_input = entry_int.get()
    km_output = (f"{mile_input} Miles is equal to {mile_input* 1.61} Kilometers")
    output_str.set(km_output)


# Window
window = ttk.Window(themename = "darkly")
window.title("Demo")
window.geometry("400x200")

# Title
title_lable = tk.Label(master = window, text = "Miles to kilometers", 
                       font = ("Times New Roman", 24, "bold"))
title_lable.pack(pady = 20)

# Input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert",
                    command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# Output
output_str = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output",
                         font = ("Times New Roman", 12, "bold"),
                         textvariable = output_str)
output_label.pack(pady = 5)

# Run
window.mainloop()
