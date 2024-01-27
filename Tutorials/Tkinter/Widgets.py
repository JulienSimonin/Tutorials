import tkinter as tk 
from tkinter import ttk

# Def buttons functions
def button_func() :
    print("a button was pressed")

def hello_func():
    print("Hello world")

# Create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk widgets
label = ttk.Label(master = window, text = "This is a test")
label.pack()

# tk.text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# Exercise label
my_label = ttk.Label(master = window, text = "My label")
my_label.pack()

# ttk button
button = ttk.Button(master = window, text = "A button", command = button_func)
button.pack()

# Exercise button
#button_hello = ttk.Button(master = window, text = "Hello", command = hello_func) # Original solution to call the function 
button_hello = ttk.Button(master = window, text = "Hello", command = lambda: print("Hello")) # Usefull alternative for easy and small function
button_hello.pack()

# Run
window.mainloop() #Update the GUI and check for events that could happen => Buttons, clicks..)

