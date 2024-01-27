import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

# Buttons

# Basic buttons :

def button_func() :
    print("A basic button")
    print(radio_var.get())
    pass

button_string = tk.StringVar(value = "A button with StringVar")

button = ttk.Button(master = window, text = "Simple Button", command = button_func,
                    textvariable = button_string) # or command = lambda: print("A simple button")
button.pack()

# Check buttons :

check_var = tk.IntVar(value = 10) # This check_var can be an IntVar for number returned or even a BooleanVar if the button just has a on/off statut
# Value = onvalue so the button will be checked when the program is launched

check = ttk.Checkbutton(master = window, text = "checkbox 1", 
                        command = lambda: print(check_var.get()),
                        variable = check_var,
                        onvalue = 10,
                        offvalue = 5 ) # Onvalue return the value when checked and Offvalue when not checked
check.pack()

check2 = ttk.Checkbutton(master = window, text = "checkbox 2", 
                        command = lambda: check_var.set(5)) # Setting the offvalue to 5 makes the two buttons connected
check2.pack()

# Radio buttons :

radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(window, text = "Radio 1", value = "radio 1",
                         variable = radio_var,
                         command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window, text = "Radio 2", value = 2,
                         variable = radio_var)
radio2.pack()

# Always assign a different value to the buttons so they are not communicating by default
# If both buttons have the same value they are going to be check at the same time and act similarly
# Only one button can be activated at a time compared to the check button that can be multiples

# Exercice :

def uncheck_buttons() :
    print(check_exercisevar.get())
    check_exercisevar.set(False)
    pass

# Data :
radio_exercisevar = tk.StringVar()
check_exercisevar = tk.BooleanVar()

# Buttons :
radio_exercise1 = ttk.Radiobutton(master = window, text = "Radio Exercise 1", 
                                 value = "A", variable = radio_exercisevar,
                                 command = uncheck_buttons)
radio_exercise1.pack()

radio_exercise2 = ttk.Radiobutton(master = window, text = "Radio Exercise 2", 
                                 value = "B", variable = radio_exercisevar,
                                 command = uncheck_buttons)
radio_exercise2.pack()

check_exercise = ttk.Checkbutton(master = window, text = "Print the Radio exercise value",
                                 variable = check_exercisevar, 
                                 command = lambda: print(radio_exercisevar.get()))
check_exercise.pack()

# Run
window.mainloop()