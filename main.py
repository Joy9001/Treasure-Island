from logo import logo
print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")

if direction != "left":
  print("You fell into a hole.\n!!! GAME OVER !!!\n")
  exit()

travel_mode = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")

if travel_mode != "wait":
  print("You were attacked by a trout.\n!!! GAME OVER !!!\n")
  exit()

door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")

if door == "red":
  print("You burned by fire.\n!!! GAME OVER !!!\n")
  exit()
elif door == "blue":
  print("You were eaten by beasts.\n!!! GAME OVER !!!\n")
  exit()
elif door == "yellow":
  print("Hurray! You found the TREASURE!!!\n")
  exit()
else:
  print("!!! GAME OVER !!!\n")
  exit()
