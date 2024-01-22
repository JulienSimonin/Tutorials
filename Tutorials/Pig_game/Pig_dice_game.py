import random
# GAME LOGIC

# Define the random roll of the dice :
def roll():
    roll = random.randint(5, 6)
    return roll

# Define the amount of players :
while True : # While loop allows to repeat the request until a valid number is entered.
    num_players = input("\nEnter the number of players (2-4) :")
    if num_players.isdigit(): # Verify that the input is a number.
        num_players = int(num_players)
        if 2 <= num_players <= 4 : # Verify that the number is between 1 and 4.
            break # Usefull to stop a while loop
        else :
            print("\nThe game only accept minimim 2 to 4 players !")
    else :
        print("\nInvalid value !\nPlease enter a valid number between 1 and 4 players.")

# Define the max score to win the game and store the score of each players in a list :
max_score = 30
player_score = [0 for _ in range(num_players)] # For the range of player, put a 0 in a list.

# Define turns logic :
while max(player_score) < max_score :
    for player_idx in range(num_players):
        print("\nPlayer", player_idx + 1, "! It's your turn !\n")
        print(f"Your current score is : {player_score[player_idx]}")
        turn_score = 0
        
        while True :
            should_roll = input("\nDo you want to roll the dice ? Yes/No : ")
            if should_roll.lower() == "yes":
                value = roll()
                if value == 1 :
                    print(f"\nOh no ! Your rolled a 1 !!\nBad luck, your turn is finished...")
                    turn_score = 0
                    break
                else :
                    print(f"\nYou rooled a : {value}")
                    turn_score += value
                    print(f"\nYour turn score is {turn_score}")
            elif should_roll.lower() == "no":
                print(f"\nYou choose to not play more turns.")
                break
            else :
                print("\nInvalid value !\nPlease don't be dumb and enter Yes or No.")
            
        player_score[player_idx] += turn_score
        print(f"\nYour current score is : {player_score[player_idx]}")

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print(f"\nWe have a winner !!...\nPlayer {winning_idx + 1} is the winner with a score of {max_score} !!!\n")
