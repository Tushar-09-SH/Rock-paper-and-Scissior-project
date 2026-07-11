import random

choices = ["ROCK", "PAPER", "SCISSORS"]

user = input("Choose ROCK, PAPER or SCISSORS: ").upper()
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("Draw!")

elif (
    (user == "ROCK" and computer == "SCISSORS")
    or (user == "SCISSORS" and computer == "PAPER")
    or (user == "PAPER" and computer == "ROCK")
):
    print("You win!")

else:
    print("Computer wins!")

print("Better luck next time!")