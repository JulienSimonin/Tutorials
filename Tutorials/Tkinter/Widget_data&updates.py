import tkinter as tk
from tkinter import ttk 

def button_func() :
    # Get the content of the entry with the get() method
    entry_text = entry.get()

    #update the label
    # label.config(text = "Some other text")
    # .configure do the same, .config is probably going to disapear
    label["text"] = entry_text # More concise and fast so better to use

    entry["state"] = "disable" # Disable or enable the widget to work

    # To know all the possibile things to change a widget
    print(label.configure())
    #{'background': ('background', 'frameColor', 'FrameColor', '', ''), 
    # 'foreground': ('foreground', 'textColor', 'TextColor', '', ''), 
    # 'font': ('font', 'font', 'Font', '', ''), 'borderwidth': ('borderwidth', 'borderWidth', 'BorderWidth', '', ''), 
    # 'relief': ('relief', 'relief', 'Relief', '', ''), 'anchor': ('anchor', 'anchor', 'Anchor', <string object: 'w'>, <string object: 'w'>), 
    # 'justify': ('justify', 'justify', 'Justify', <string object: 'left'>, <string object: 'left'>), 
    # 'wraplength': ('wraplength', 'wrapLength', 'WrapLength', '', ''), 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', ''), 
    # 'text': ('text', 'text', 'Text', '', ''), 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 
    # 'underline': ('underline', 'underline', 'Underline', -1, -1), 'width': ('width', 'width', 'Width', '', ''), '
    # image': ('image', 'image', 'Image', '', ''), 'compound': ('compound', 'compound', 'Compound', '', ''), 
    # 'padding': ('padding', 'padding', 'Pad', '', ''), 'state': ('state', 'state', 'State', <string object: 'normal'>, <string object: 'normal'>), 
    # 'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'style': ('style', 'style', 'Style', '', ''), 'class': ('class', '', '', '', '')}

# Window
window = tk.Tk()
window.title("Getting and setting widget")
window.geometry("800x500")

# Widgets
label = ttk.Label(master = window, text = "Collect the data")
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = "Get the data", command = button_func)
button.pack()

# Exercise
# ADD another buttonthat change the text back to "some text" and enables entry to work

def reset() :
    label["text"] = "Some text"
    entry["state"] = "enable"

reset_button = ttk.Button(master = window, text = "Reset", command = reset)
reset_button.pack()

# Run
window.mainloop()