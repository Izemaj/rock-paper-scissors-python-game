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

game = [rock,paper,scissors]
print('Welcome to Rock,Paper,Scissors game!')
print('Rules of the game:\nRock wins against scissors.\nScissors win against paper.\nPaper wins against rock.\nSame choice is a draw.')
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice < 3:
  print(game[user_choice])
  computer_choice = random.randint(0,2)
  print(f"Computer chose {computer_choice} !")
  print(game[computer_choice])
  if game[user_choice] == game[computer_choice]:
    print("It's a draw")
  elif game[user_choice] == rock and game[computer_choice] == scissors:
    print('You won!')
  elif game[user_choice] == scissors and game[computer_choice] == paper:
    print('You won!')
  elif game[user_choice] == paper and game[computer_choice] == rock:
    print('You won!')
  elif game[computer_choice] == rock and game[user_choice] == scissors:
    print('Computer won!')
  elif game[computer_choice] == scissors and game[user_choice] == paper:
    print('Computer won!')
  elif game[computer_choice] == paper and game[user_choice] == rock:
    print('Computer won!')
else:
  print('Wrong input! You lose!')
