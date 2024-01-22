import tkinter as tk 
from tkinter import ttk 

def convert () :
    print(entryInt.get())

# Window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")

# Title
title_lable = tk.Label(master = window, text = "Miles to kilometers", 
                       font = ("Times New Roman", 24, "bold"))
title_lable.pack()

# Input field
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text = "Convert",
                    command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# Output
output_label = ttk.Label(master = window, text = "Output",
                         font = ("Times New Roman", 14, "bold"))
output_label.pack(pady = 5)

# Run
window.mainloop()
