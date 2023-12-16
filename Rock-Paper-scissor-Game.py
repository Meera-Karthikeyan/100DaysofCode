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

#Write your code below this line 👇

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
player_input = int(input())

if player_input == 0:
  print(rock)
elif player_input == 1:
  print(paper)
elif player_input == 2:
  print(scissors)
else:
  print("Invalid")

print("Computer chose:")

computer_input = random.randint(0,2)

if computer_input == 0:
  print(rock)
elif computer_input == 1:
  print(paper)
elif computer_input == 2:
  print(scissors)
else:
  print("Invalid")

if player_input == 0:
  if computer_input == 1:
    print("You lose")
  elif computer_input == 2:
    print("You Win")
  else:
    print("Draw, Try Again.")
elif player_input == 1:
  if computer_input == 0:
    print("You win")
  elif computer_input == 2:
    print("You lose")
  else:
    print("Draw, Try Again.")
elif player_input == 2:
  if computer_input == 0:
    print("You lose")
  elif computer_input == 1:
    print("You Win")
  else:
    print("Draw, Try Again.")
else:
  print("Game Over")
