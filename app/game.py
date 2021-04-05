
from random import choice

def determine_winner(c,u):

    if u == c:
        out = "It's a tie!"

    elif u == "rock" and c == "paper":
        out = "The computer wins"
    elif u == "rock" and c == "scissors":
        out = "The user wins"

    elif u == "paper" and c == "scissors":
        out = "The computer wins"
    elif u == "paper" and c == "rock":
        out = "The user wins"

    elif u == "scissors" and c == "rock":
        out = "The computer wins"
    elif u == "scissors" and c == "paper":
        out = "The user wins"

    return out

#
# USER SELECTION
#
if __name__ == "__main__":
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

    result = determine_winner(c,u)
    print(result)
