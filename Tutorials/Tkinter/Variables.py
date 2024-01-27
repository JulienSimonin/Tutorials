import tkinter as tk 
from tkinter import ttk 

def button_func() :
    string_var.set("Button Pressed") # Set the value of the variable to something else
    print(string_var.get()) # Print the value

# Window
window = tk.Tk()
window.title("Tkinter variables")

# Tkinter variable
string_var = tk.StringVar(value = "Enter your variable")

# Also exist IntVar, DoubleVar, BooleanVar

# Widgets
label = ttk.Label(master = window, text = "Enter your Text", 
                  textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

# Several entry can be connected to the same variable and thus change the label but also each other entry
entry2 = ttk.Entry(master = window, textvariable = string_var)
entry2.pack()

button = ttk.Button(master = window, text = "button", 
                    command = button_func)
button.pack()

exercise_var = tk.StringVar(value = "Test")

entry_exercise1 = ttk.Entry(master = window, textvariable = exercise_var)
entry_exercise1.pack()

entry_exercise2 = ttk.Entry(master = window, textvariable = exercise_var)
entry_exercise2.pack()

label_exercise = ttk.Label(master = window, text = "Enter your Text", 
                  textvariable = exercise_var)
label_exercise.pack()

# Run
window.mainloop()