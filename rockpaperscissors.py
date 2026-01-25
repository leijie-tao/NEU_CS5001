# CS 5001, Assignment #3 Rock, Paper, Scissors Game
# DO NOT use AI tools while working on this assignment.

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
_______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
            ______)
         __________)
      (____)
---.__(___)
"""
ASCIIart = [rock, paper, scissors] 
names = ["rock", "paper", "scissors"] 
# TO DO: Print the title of the game and/or welcome message
print("Welcome to the Rock-Paper-Scissors game!")
# TO DO: Prompt the user for input (0, 1, 2)
try: 
    user_choice = int(input("What is your choice? Please type 0 for rock, 1 for paper, and 2 for scissors.\n"))
# TO DO: Print ASCII art for user's choice
    print(f"You chose {names[user_choice]}.\n {ASCIIart[user_choice]}")
except: 
    print("Invalid input. Please run and choose again.")
    exit()    
# TO DO: Generate computer choice
computer_choice = random.randint(0,2) 
# TO DO: Print ASCII art for computer's choice
print(f"Computer chose {names[computer_choice]}.\n {ASCIIart[computer_choice]}")
# TO DO: Decide winner using conditionals
# TO DO: Print result
if user_choice == computer_choice: 
    print("It's a tie.")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
        print("You win!") 
else:
     print("You lose.")
