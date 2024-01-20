#%%
num_1 = int(input("What is the first number? "))
num_2 = int(input("What is the second number? "))
if num_1 > num_2:
    print("The first number is greater.")
else:
    print("The first number is not greater.")
if num_1 == num_2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
if num_1 < num_2:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

print()
animal = input("What is your favorite animal? ")

if animal.lower() == "dog":
    print("That is my favorite animal too!")
else:
    print("That is not my favorite animal")
#%%