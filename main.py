# 1 for rock,
# -1 for paper,
# 0 for scissors

import random

computer = random.choice([-1, 0, 1])  # Random choice for computer

youstr = input("Enter your choice (r for rock, p for paper, s for scissors): ")  # Input from user
youDict = {"r": 1, "p": -1, "s": 0} # Dictionary for user input
reverseDict = {1: "r", -1: "p", 0: "s"} # Reverse dictionary for output

print(f"computer choice: {reverseDict[computer]}") # Print computer choice
print(f"your choice: {youstr}") # Print user choice

# code

if youstr not in youDict:
    print("Invalid input")
else:
    you = youDict[youstr]

    if (computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
        print("You win")
    elif computer == you:
        print("Draw")
    else:
        print("You lose")