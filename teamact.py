#%%
word = "commitment"
letter = input("What is your favorite letter? ")
for i in word:
    if i == letter:
        print(f"_", end="")
    else:
        print(f"{i}", end="")

