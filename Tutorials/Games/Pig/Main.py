from tkinter import *
from tkinter import ttk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

game_menu = Tk()
game_menu.geometry("800x500")
game_menu.title("Game")
game_menu.resizable(False, False)
game_menu["bg"] = "#FDF1B8"
center_window(game_menu, 800, 500)

title = Label(game_menu, text = "Welcome to the Pig Dice Game !", bg = "#FDF1B8", 
            font = ("Times New Roman", 30, "bold"))
title.pack(pady = 120)

exit_button = Button(game_menu, text = "Exit", bg = "#FDF1B8", command = game_menu.destroy, 
                        font = ("Times New Roman", 20, "bold"))
exit_button.pack(side = BOTTOM, fill = "x")

def game_window () :
    game_menu.withdraw()
    game = Tk()
    center_window(game, 800, 500)
    game.geometry("800x500")
    game.resizable(False, False)
    game.title("Game")
    game["bg"] = "#FDF1B8"

    def back_to_main_menu():
        game_menu.deiconify()
        game.destroy()
    
    def start_game(player_count):
        print(f"\nStarting game with {player_count} players!")

    error_number = Label(game, bg = "#FDF1B8", font = ("Times New Roman", 15, "bold"))

    error_dumb = Label(game, bg = "#FDF1B8", font = ("Times New Roman", 15, "bold"))

    def get_player_count():
        player_count = input_area.get()

        error_number.config(text="")
        error_dumb.config(text="")
        
        if player_count.isdigit():
            player_count = int(player_count)
            if 2 <= player_count <= 4:
                start_game(player_count)
            else :
                error_number.config(text = "The game only accept minimim 2 to 4 players !", fg = "red")
                error_number.pack()
        else :
            error_dumb.config(text = "Invalid value !\nPlease enter a number between 2 and 4 players.", fg = "red")
            error_dumb.pack()

    player_selection_label = Label(game, text = "Enter the number of players (2-4) :",
                             bg = "#FDF1B8", font = ("Times New Roman", 30, "bold"))
    player_selection_label.pack(side = TOP, pady = 50)

    input_area = Entry(game, font=("Times New Roman", 15), width=10)
    input_area.pack(side = TOP, pady = 20)

    start_game_button = Button(game, text="Start Game", bg="#FDF1B8", 
                               command=get_player_count, font=("Times New Roman", 30, "bold"))
    start_game_button.pack()

    quit_button = Button(game, text = "Quit Game", bg = "#FDF1B8", command = game.destroy, 
                        font = ("Times New Roman", 20, "bold"))
    quit_button.pack(side= BOTTOM, pady = 10)
    
    back_button = Button(game, text = "Back to main Menu", bg = "#FDF1B8", 
                        command = back_to_main_menu, 
                        font = ("Times New Roman", 20, "bold"))
    back_button.pack(side= BOTTOM, pady = 10)
    
    game.mainloop()

play_button = Button(game_menu, text = "Play the game", bg = "#FDF1B8", command =game_window,
                        font = ("Times New Roman", 25, "bold"))
play_button.pack(side = TOP)

game_menu.mainloop()
