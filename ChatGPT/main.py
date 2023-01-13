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

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Print the computer's choice
def print_computer_choice(computer_choice):
    print("Computer chose:")
    print(choices[computer_choice])

# Play method compare all possible combinations of play and prints the results.
def play(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Tied!")
    elif player_choice == 0 and computer_choice == 1:
        print("Rock vs Paper!\nYou Lose")
    elif player_choice == 0 and computer_choice == 2:
        print("Rock vs Scissors!\nYou Win!")
    elif player_choice == 1 and computer_choice == 0:
        print("Paper vs Rock!\nYou Win!")
    elif player_choice == 1 and computer_choice == 2:
        print("Paper vs Scissors!\nYou Lose")
    elif player_choice == 2 and computer_choice == 0:
        print("Scissors vs Rock!\nYou Lose")
    elif player_choice == 2 and computer_choice == 1:
        print("Scissors vs Paper!\nYou Win!")

# Handle the play again prompt
def play_again():
    while True:
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y" or play_again == "n":
            return play_again.lower() == "y"
        else:
            print("Invalid input, please enter 'y' or 'n'.")

while True:
    # Intro
    print("Welcome To Rock, Paper, Scissors\n")

    # Loop to guarantee User's input is either 0-2. Will continue to loop until 0-2 is entered.
    while True:
        try:
            player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
            if player_choice not in range(3):
                raise ValueError
            print(choices[player_choice])
            break
        except ValueError:
            print(f"Invalid input. Please enter a number between 0 and 2.")

    computer_choice = random.randint(0, 2)
    print_computer_choice(computer_choice)

    play(player_choice, computer_choice)

    if not play_again():
        break