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

# 0 = rock
# 1 = paper
# 2 = scissors

while True:
  print("Welcome To Rock, Paper, Scissors\n")

  while True:
    players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
    if players_choice.isdigit() and 0 <= int(players_choice) <= 2:
      if players_choice == "0":
        print(rock)
      elif players_choice == "1":
        print(paper)
      else:
        print(scissors)
      break
    else:
      print(f"You entered {players_choice} which is invalid.\n")



  computers_choice = random.randint(0,2)
  print("Computer chose:")

  if computers_choice == 0:
    print(rock)
  elif computers_choice == 1:
    print(paper)
  elif computers_choice == 2:
    print(scissors)

  def play(players_choice, computers_choice):
      if players_choice == "0" and computers_choice == 1:
          print("Rock vs Paper!\nYou Lose")
      elif players_choice == "0" and computers_choice == 2:
          print("Rock vs Scissors!\nYou Win!")
      elif players_choice == "1" and computers_choice == 0:
          print("Paper vs Rock!\nYou Win!")
      elif players_choice == "1" and computers_choice == 2:
          print("Paper vs Scissors!\nYou Lose")
      elif players_choice == "2" and computers_choice == 0:
          print("Scissors vs Rock!\nYou Lose")
      elif players_choice == "2" and computers_choice == 1:
          print("Scissors vs Paper!\nYou Win!")
      else:
          print("Tied!")
          
  play(players_choice, computers_choice)
  play_again = input("Do you want to play again? (y/n) ")
  if play_again.lower() == "n":
      break
  elif play_again.lower() != "y":
      print("Invalid input. Please enter 'y' or 'n'.")