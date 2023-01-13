import random


# ASCII images for Rock, Paper, and Scissors.
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

# 0 = rock
# 1 = paper
# 2 = scissors

# While Loop gives User the option to play again.
# Game Starts
while True:
  # Intro
  print("Welcome To Rock, Paper, Scissors\n")

  # While Loop to guarantee User's input is either 0-2. Will continue to loop until 0-2 is entered.
  while True:
    players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

    # Makes sure the input is a digit and is between 0-2
    if players_choice.isdigit() and 0 <= int(players_choice) <= 2:

      # Print ASCII image of choosen play.
      if players_choice == "0":
        print(rock)
      elif players_choice == "1":
        print(paper)
      else:
        print(scissors)
      break

    # Alert User their input was invalid, While Loop restarts.
    else:
      print(f"You entered {players_choice} which is invalid.\n")

  # Get a random int 0-2 for the computers choice.    
  computers_choice = random.randint(0,2)

  # Print the computers choice.
  print("Computer chose:")

  # Print ASCII image
  if computers_choice == 0:
    print(rock)
  elif computers_choice == 1:
    print(paper)
  elif computers_choice == 2:
    print(scissors)

  # Play method compare all possible combinations of play and prints the results.
  def Play(players_choice, computers_choice):
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

  # Play method is called with the players_choice and computers_choise passed to it.        
  Play(players_choice, computers_choice)

  # Ask User if they want to play again.
  while True:
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y" or play_again == "n":
        break
    else:
        print("Invalid input, please enter 'y' or 'n'.")
    
  if play_again.lower() == "n":
      break
  elif play_again.lower() != "y":
      print("Invalid input. Please enter 'y' or 'n'.")