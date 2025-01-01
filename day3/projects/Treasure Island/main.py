print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

                       {}           {}
                         \  _---_  /
                          \/     \/
                           |() ()|
                            \ + /
                           / HHH  \\
                          /  \_/   \\
                        {}          {}


''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure")

start = input("Are you ready to join the adventure? yes/no\n").lower()

if not start == "yes":
  print("Come back when you're ready")
  exit(1)

crossroad_direction = input("Great! Let's not wait any time and start our adventure right away.\nYou're at a crossroad, are you going left or right?\n")

print("Walking....")

if not crossroad_direction == "left":
  print(f"You've decided to go {crossroad_direction}, after walking for a short while you fall into a hole, break your leg and die from the injury!")
  exit(1)

print("The path was hard but you now have arrived on the coast. You need to get to the house on the island you see.\nThere is a ferry service to take you there, however the boat won't be here for another 5 hours.")

island_choice = input("Do you want to wait or swim accross?\n").lower()

if not island_choice == "wait":
  if island_choice == "swim":  
    print(f"Swimming....\nAfter swimming for 15 mins, you're attacked by a giant trout, panick and drown!\nGame Over")
    exit(1)
  print(f"{island_choice} was not an given option.\nNo cheats allowed!\nGame Over")
  exit(1)

print("Waiting...\nThe boat is 2 hours late, after the short crossing you make your way to the house. The house has 3 doors, a red one, a blue one and a yellow one.")

door_choice = input("Which colour do you pick?\n").lower()

if door_choice == "red":
  print("As soon as you enter the room, the door closes behind you.\nThe room is now on fire.\nYou can't escape and get burned.\nGame Over")
  exit(1)
elif door_choice == "blue":
  print("When opening the door, a wild beast jumps on you and eats you.\Game Over")
  exit(1)
elif door_choice == "yellow":
  print("You enter the room, loads of people start clapping and offer you the island most precious tresure, a ice cream!")
  exit(1)
else:
  print(f"{door_choice} was not an given option.\nNo cheats allowed!\nGame Over")
  exit(1)