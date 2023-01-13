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
print("Welcome To Rock, Paper, Scissors\n")
players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

if players_choice == "0":
  print(rock)
elif players_choice == "1":
  print(paper)
else:
  print(scissors)

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
        print("You Lose")
    elif players_choice == "0" and computers_choice == 2:
        print("You Win!")
    elif players_choice == "1" and computers_choice == 0:
        print("You Win!")
    elif players_choice == "1" and computers_choice == 2:
        print("You Lose")
    elif players_choice == "2" and computers_choice == 0:
        print("You Lose")
    elif players_choice == "2" and computers_choice == 1:
        print("You Win!")
    else:
        print("Tied!")
        
play(players_choice, computers_choice)        