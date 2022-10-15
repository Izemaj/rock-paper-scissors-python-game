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
# Create a list of the above play options
game = [rock,paper,scissors]
print('Welcome to Rock,Paper,Scissors game!')
print('Rules of the game:\nRock wins against scissors.\nScissors win against paper.\nPaper wins against rock.\nSame choice is a draw.')

# Collect the User's Choice
user_choice = game[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))]
# Generate the computer's choice by assigning a random integer
computer_choice = game[random.randint(0,2)]
if user_choice < 3:
  print(game[user_choice])
  print(f"Computer chose {computer_choice} !")
  print(game[computer_choice])
  if user_choice == computer_choice:
    print("It's a draw")
  elif user_choice == rock and computer_choice == scissors:
    print('You won!')
  elif user_choice == scissors and computer_choice == paper:
    print('You won!')
  elif user_choice == paper and computer_choice == rock:
    print('You won!')
  elif computer_choice == rock and user_choice == scissors:
    print('You lose!')
  elif computer_choice == scissors and user_choice == paper:
    print('You lose!')
  elif computer_choice == paper and user_choice == rock:
    print('You lose!')
else:
  print('Wrong input! You lose!')
