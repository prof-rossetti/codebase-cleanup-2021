
from random import choice

#
# USER SELECTION
#
def determine_winner(u, c):
    
    if u == "rock" and c == "rock":
        print("It's a tie!")
    elif u == "rock" and c == "paper":
        print("The computer wins")
    elif u == "rock" and c == "scissors":
        print("You've won!")
    elif u == "paper" and c == "rock":
        print("You've won!")
    elif u == "paper" and c == "paper":
        print("It's a tie!")
    elif u == "paper" and c == "scissors":
        print("The computer wins")

    elif u == "scissors" and c == "rock":
        print("The computer wins")
    elif u == "scissors" and c == "paper":
        print("You win!")
    elif u == "scissors" and c == "scissors":
        print("It's a tie!")


VALID_OPTIONS = ["rock", "paper", "scissors"]

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#
determine_winner(u, c)