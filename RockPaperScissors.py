import random

choices = ["rock", "paper", "scissors"]
user = input("Do you want to throw rock, paper or scissors? ")
computer_choice= random.randint(0,2)
user_choice = choices.index(user.lower())
print(f"Your opponent throws {choices[computer_choice]}")
if user_choice-computer_choice == 1:
    print("You win!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw.")
else:
    print("You lose!")
