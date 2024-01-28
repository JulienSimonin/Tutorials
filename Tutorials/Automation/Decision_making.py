# Import random and choose a random proposition inside a list
from random import choice

anime_list = ["SNK", "Death note", "One piece", "JJKS", "Demon slayer"]

see_my_list = input("Do you want to see your anime list ? Yes/No\n")

def see_list():
    if see_my_list == "Yes":
        print(anime_list)
        return update_list()
    elif see_my_list == "No":
        return update_list()
    else:
        return "You entered a wrong value !"

def update_list():
    new_list = input("Do you want to add an anime to your watch list ? Yes/No \n")
    if new_list == "Yes" :
        user_input = input("Enter the anime(s) you want to add separated by a coma :\n")
        user_list = user_input.split(", ")
        updated_list = user_list + anime_list
        new_updated_list = set(updated_list + user_list)
        print(f"Here is your updated anime list !\n{new_updated_list}")
        loop_choice = input("Do you want to choose between animes of this list ? Yes/No\n")
        if loop_choice == "Yes":
            return f"The algorytm choose that you're going to watch {choice(updated_list)}."
        else :
            return update_list()
    elif new_list == "No" :
        return choice(anime_list)
    else :
        return "You entered wrong characters !"

decision = see_list()
print(decision)