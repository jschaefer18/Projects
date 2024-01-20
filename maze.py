print("Welcome to Josh's Maze!")
print("Directions: N = (North) S = (South) E = (East) W = (West)")
go = True
def room_one():
   dir = input("Would you like to go N, S, E, or W? ")
   if dir.upper() == "N":
       print("You have hit a wall.")
   elif dir.upper() == "S":
       print("You have hit a wall.")
   elif dir.upper() == "E":
       print("You have hit a wall.")
   elif dir.upper() == "W":
       print("Congrats you have moved into room 2!")
       room_two()
       go = False

def room_two():
    print("Welcome to room two")
    

while go:
    room_one()

