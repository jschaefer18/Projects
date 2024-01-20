print("Welcome to Wordle!")
print("Rules: Your guess must be five characters long. For example, 'trace'.")
secret = "beach"
num_guesses = 0
complete_word = ""
while True:
    guess = input("What is your guess? ").lower()

    if len(guess) != 5:
        print("Your guess must be five characters long.")
        continue
    num_guesses += 1

    if guess == secret:
        print(f"Congratulations! You guessed the word '{secret}' in {num_guesses} attempts.")
        break

    for i in range(5):
        if guess[i] == secret[i]:
            complete_word += guess[i].upper() # this is saying that if the fist letter in guess and first letter in secret are equal to add the capitol first letter of guess to the complete word.
        elif guess[i] in secret:
            complete_word += guess[i].lower()
        else:
            complete_word += "_"

    print(complete_word)
