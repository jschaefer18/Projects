#%%

import random
run = True

while run == True:
    guess_num = -1
    magic_num = random.randint(1,101)
    number_guesses = 0
    while magic_num != guess_num:
        guess_num = int(input('What is your guess?' ))
        if magic_num < guess_num:
            print("Lower")
            number_guesses = number_guesses + 1
        if magic_num > guess_num:
            print("Higher")
            number_guesses = number_guesses + 1
        if magic_num == guess_num:
            number_guesses = number_guesses + 1
            print("Congrats you guessed the number!")
            print(f"You beat the game in {number_guesses} tries!")
            answer = input("Do you want to play again? ")
            if answer.upper() == "YES":
                print("You keep playing!")
            if answer.upper() == "NO":
                print("Goodbye:(")
                run = False
            

# %%
