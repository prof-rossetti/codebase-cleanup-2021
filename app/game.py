
from random import choice

def determine_winner(c,u):
    w = "The user wins"
    l = "The computer wins"

    if u == c:
        out = "It's a tie!"

    elif u == "rock":
        if c == "paper":
            out = l
        elif c == "scissors":
            out = w

    elif u == "paper":
        if c == "scissors":
            out = l
        elif c == "rock":
            out = w

    elif u == "scissors":
        if c == "rock":
            out = l
        elif c == "paper":
            out = w

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
