import random
num = random.randint(1,100)
num_guesses = 0
is_guessed = False

while is_guessed == False:
    guessed_num = int(input("Guess a number 1 to 100: "))
    if guessed_num < num:
        print("Guess higher!")
        num_guesses = num_guesses + 1
    elif guessed_num > num:
        print("Guess lower! ")
        num_guesses = num_guesses + 1
    elif guessed_num == num:
        is_guessed = True
        num_guesses = num_guesses + 1
        print(f"You win! It took you {num_guesses} tries.")
    