import random
# These are the  options for the user
options=["snake","water","gun"]
# It will show the options
print(options)

# It will take  the input from the user
user_input=input("select your option :")

# This will enable the  computer to select random options from the options list
computer_input=random.choice(options)

# It will print the computer option
print("The computer option is",computer_input)

# This block  of code is the core of the game as it is the main logic of code
if user_input == computer_input:
    print("It's a draw!")

elif user_input == "snake" and computer_input == "water":
    print("You win! Snake drinks water ")

elif user_input == "water" and computer_input == "snake":
    print("Computer wins! Snake drinks water ")

elif user_input == "water" and computer_input == "gun":
    print("You win! Water sinks gun ")

elif user_input == "gun" and computer_input == "water":
    print("Computer wins! Water sinks gun ")

elif user_input == "gun" and computer_input == "snake":
    print("You win! Gun kills snake ")

elif user_input == "snake" and computer_input == "gun":
    print("Computer wins! Gun kills snake ")

else:
    print("Invalid input! Please choose snake, water, or gun.")




