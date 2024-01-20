#%%
print("Please enter the following: ")
print()
name = input("Name: ")
adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")
animal2 = input("Animal: ")
negverb = input("Negative verb: ")
superhero = input("Superhero: ")
a = "a"
if animal2[0].lower() in ["o","a","e","u","i"]:
    a = "an"
print()
print("Your story is:")
print()
print(f"""My name is {name} and the other day, I was really in trouble. It all started when I saw a very {adjective} \
{animal} {verb} down the hallway. {exclamation} I yelled. But all I could think to do was to {verb2} \
over and over. Miraculously, that caused the {animal} to stop, but not before it tried to {verb3} right \
in front of my family. I thought it was over until I saw {a} {animal2}. Shivering in fear all I could do was {negverb}.\
In my last breathes {superhero} swooped in and saved me. I ended up getting an autograph and 1 million dollars. The end""")


