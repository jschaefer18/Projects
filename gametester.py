global distance
distance = 100
global game_key
game_key = False
global amount_moves
amount_moves = 0
print()
print("Welcome to Josh's Adventure Game!")
print("Rules:")
print("Write whatever choice you want based on the capitalized words.")
print("For example if it said NORTH or SOUTH. You would type either NORTH or SOUTH.")
print("Context:")
print("You are being chased by a dangerous monster. As you are running from it you aproach a maze. You must treverse this maze and escape him.")
print("")
 
def room_one(game_key,distance,amount_moves):
    key_1 = True
    while key_1:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_one = input("You are in Room ONE. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_one.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into room two.")
            key_1 = False
            room_two(game_key,distance,amount_moves)
        elif choice_one.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_one.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_one.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk back into the creature and die.") # If you walk back towards the creature the game just straight up ends.
            exit()
        else:
            print("Invalid input please try again.")

def room_two(game_key,distance,amount_moves):
    key_2 = True
    while key_2:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_two = input("You are in Room TWO. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_two.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_two.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk back into room one.")
            distance = distance - 10
            room_one(game_key,distance,amount_moves) # This makes it so you walk back into room one.
        elif choice_two.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into room three.")
            key_2 = False
            room_three(game_key,distance,amount_moves)
        elif choice_two.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        else:
            print("Invalid input please try again.")


def room_three(game_key,distance,amount_moves):
    key_3 = True
    while key_3:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_three = input("You are in Room THREE. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_three.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into wall.")
            distance = distance - 5
        elif choice_three.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_three.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into room four.")
            key_3 = False
            room_four(game_key,distance,amount_moves)
        elif choice_three.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk back into room two.")
            distance = distance - 10
            room_two(game_key,distance,amount_moves)
        else:
            print("Invalid input please try again.")


def room_four(game_key,distance,amount_moves):
    key_4 = True
    while key_4:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_four = input("You are in Room FOUR. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_four.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_four.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into room five.")
            key_4 = False
            room_five(game_key,distance,amount_moves)
        elif choice_four.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_four.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk back into room three.")
            distance = distance - 10
            room_three(game_key,distance,amount_moves)
        else:
            print("Invalid input please try again.")


  
    
def room_five(game_key,distance,amount_moves):
    key_5 = True
    while key_5:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_five = input("You are in Room FIVE. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_five.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk back into room four.")
            distance = distance - 10
            room_four(game_key,distance,amount_moves)
        elif choice_five.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into room six.")
            key_5 = False
            room_six(game_key,distance,amount_moves)
        elif choice_five.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_five.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        else:
            print("Invalid input please try again.")



def room_six(game_key,distance,amount_moves):
    key_6 = True
    while key_6:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_six = input("You are in Room SIX. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_six.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk back into room five.")
            distance = distance - 10
            room_five(game_key,distance,amount_moves)
        elif choice_six.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_six.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_six.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk into room seven.")
            key_6 = False
            room_seven(game_key,distance,amount_moves)
        else:
            print("Invalid input please try again.")

            

def room_seven(game_key,distance,amount_moves):
    key_7 = True
    while key_7:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_seven = input("You are in Room SEVEN. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_seven.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into room eight.")
            distance = distance - 5
            key_7 = False
            room_eight(game_key,distance,amount_moves)
        elif choice_seven.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_seven.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk back into room six.")
            distance = distance - 10
            room_six(game_key,distance,amount_moves)
        elif choice_seven.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk into room nine.")
            key_7 = False
            room_nine(game_key,distance,amount_moves)
        else:
            print("Invalid input please try again.")


def room_eight(game_key,distance,amount_moves):
    key_8 = True
    while key_8:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        want_key = input("As you walk into room right you see a key on the ground. Type CLAIM if you want this key? ")
        if want_key.upper() == "CLAIM":
            print("Congrats you claimed the key!")
            game_key = True

        
        choice_eight = input("You are in Room EIGHT. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_eight.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_eight.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk back into room seven.")
            distance = distance - 10
            room_seven(game_key,distance,amount_moves)
        elif choice_eight.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_eight.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        else:
            print("Invalid input please try again.")


    
    

def room_nine(game_key,distance,amount_moves):
    key_9 = True
    while key_9:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_nine = input("You are in Room NINE. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_nine.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into room ten.")
            room_ten(game_key,distance,amount_moves)
        elif choice_nine.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_nine.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk back into room seven.")
            distance = distance - 10
            room_seven(game_key,distance,amount_moves)
        elif choice_nine.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        else:
            print("Invalid input please try again.")



def room_ten(game_key,distance,amount_moves):
    key_10 = True
    while key_10:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_ten = input("You are in Room TEN. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_ten.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk back into room nine.")
            distance = distance - 10
            room_nine(game_key,distance,amount_moves)
        elif choice_ten.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_ten.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into room eleven.")
            room_eleven(game_key,distance,amount_moves)
        elif choice_ten.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        else:
            print("Invalid input please try again.")


def room_eleven(game_key,distance,amount_moves):
    key_11 = True
    while key_11:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_eleven = input("You are in Room ELEVEN. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_eleven.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_eleven.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_eleven.upper() == "NORTH":
            amount_moves = amount_moves + 1
            print("You walk into room twelve.")
            room_twelve(game_key,distance,amount_moves)
        elif choice_eleven.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk back into room ten.")
            room_ten(game_key,distance,amount_moves)
        else:
            print("Invalid input please try again.")


def room_twelve(game_key,distance,amount_moves):
    key_12 = True
    print("As you walk into room TWELVE you see a locked door to the NORTH.")
    while key_12:
        if distance <= 0:
            game_over()
        print(f"The monster is {distance}m away!")
        choice_twelve = input("You are in Room TWELVE. Would you like to go NORTH SOUTH EAST or WEST? ")
        if choice_twelve.upper() == "WEST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_twelve.upper() == "EAST":
            amount_moves = amount_moves + 1
            print("You walk into a wall.")
            distance = distance - 5
        elif choice_twelve.upper() == "NORTH" and game_key == True:
            amount_moves = amount_moves + 1
            print("Hooray!")
            game_win(distance,amount_moves)
        elif choice_twelve.upper() == "NORTH" and game_key == False:
            amount_moves = amount_moves + 1
            print("You try going through the door, but can't because you have not obtained the key. Try going West in room seven.")
            distance = distance - 5
        elif choice_twelve.upper() == "SOUTH":
            amount_moves = amount_moves + 1
            print("You walk back into room eleven.")
            distance = distance - 10
            room_eleven(game_key,distance,amount_moves)
        else:
            print("Invalid input please try again.")


        


def game_win(distance,amount_moves):
    print("Congrats you have beaten my game!")
    print(f"You completed the game in {amount_moves} moves!")
    print(f"In the end the monster was {distance}m away from you.")
    exit()

def game_over(): # use if distance is less than or equal to 0
    print("Game Over!")
    print("The monster has caught you.")
    exit()

room_one(game_key,distance,amount_moves)





