# command that allow the computer to make random decisions. 
# The ready-made pictures of stone, paper and numbers were taken from the following website: https://ascii.co.uk/art

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# I want that in the solution that the images will be presented  
game_images = [rock, paper, scissors]

# imput to out choise in the game.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

# random command to the computer to make a move. We have only 3 options to chose, so the randint is from 0 to 2 (int the computer world we count in binary that starts with 0 count).
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Loops that examine all the options of the game and their result
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

