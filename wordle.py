#%%
print("Welcome to Wordle!")
print("Rules: Your guess must be five characters long. For example, 'trace'.")
secret = "beach"
num_guesses = 0

while True:
    guess = input("What is your guess? ").lower()
    complete_word = ""  # Reset complete_word for each new guess

    if len(guess) != 5: # This checks if the input for guess is not equal to 5. If it is not 5 character long it will make you input again until it is the length of 5
        print("Your guess must be five characters long.")
        continue
    num_guesses += 1

    if guess == secret:
        print(f"Congratulations! You guessed the word '{secret}' in {num_guesses} attempts.")
        break

    for i in range(5):
        if guess[i] == secret[i]: # this is saying that if the fist letter in guess and first letter in secret are equal to add the capitol first letter of guess to the complete word.
            complete_word += guess[i].upper() + " " # this adds a space between the underscore
        elif guess[i] in secret:
            complete_word += guess[i].lower() + " " # this adds a space between the underscore
        else:
            complete_word += "_ " # this adds a space between the underscore

    print(complete_word)


# %%
