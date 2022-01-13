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

image = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if player_choice > 2 or player_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(image[player_choice])

  pc_choice = random.randint(0, 2)
  print("Computer chose:")
  print(image[pc_choice])

  if player_choice == pc_choice:
    print("It's a draw.")
  elif player_choice == 2 and pc_choice == 0:
    print("You lose!")
  elif player_choice == 0 and pc_choice == 2:
    print("You win!")
  elif player_choice > pc_choice:
    print("You win!")
  else:
    print("You lose!")
