
from random import choice

def determine_winner(c,u):
    if u == c:
        print("It's a tie!")

    elif u == "rock":
        if c == "paper":
            print("The computer wins")
        elif c == "scissors":
            print("The user wins")

    elif u == "paper":
        if c == "scissors":
            print("The computer wins")
        elif c == "rock":
            print("The user wins")

    elif u == "scissors":
        if c == "rock":
            print("The computer wins")
        elif c == "paper":
            print("The user wins")


#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
choices = ["rock", "paper", "scissors"]
if u not in choices:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(choices)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

determine_winner(c,u)
