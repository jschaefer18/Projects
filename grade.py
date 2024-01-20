grade = float(input("What is your grade? "))
letter = ""
a_an = "a"
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"



last_digit = grade % 10 # This will give us the last digit of the grade
sign = ""
if last_digit >= 7:
   sign =  "+"
elif last_digit < 3:
    sign = "-"

if letter == "A": # This checks if you should use an or a
    a_an = "an"

if letter == "A" and sign == "+": # This makes it so A+ do not exist
    sign = ""

if letter == "F":
    sign = ""

print(f"You have {a_an} {letter}{sign}.")



if grade >= 70:
    print("Congrats you pass the class!")
else: 
    print("You're trash get better.")