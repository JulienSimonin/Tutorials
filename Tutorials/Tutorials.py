import random

def get_choices():
    player_choice = input("Enter a choice between rock, paper or scissors : \n")
    options = ["rock", "paper", "scissors"]
    computer_choice = "The choice of the computer is " + random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player} and the computer chose {computer}")
    if player == computer:
        return "It's a tie !"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes the scissors ! You win !"
        else :
            return "Paper covers the rock ! You loose..."
    elif player == "paper":
        if computer == "scissors":
            return "Paper gets cut by the scissors !! You loose..."
        else :
            return "Paper covers the rock ! You win..."
    elif player == "scissors":
        if computer == "paper":
            return "Paper gets cut by the scissors !! You win !"
        else :
            return "Rock smashes the scissors ! You loose..."


