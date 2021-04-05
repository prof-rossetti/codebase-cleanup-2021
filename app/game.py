
from random import choice

def determine_winner(c,u):
    w = "The user wins"
    l = "The computer wins"

    if u == c:
        return "It's a tie!"

    elif u == "rock":
        if c == "paper":
            return l
        elif c == "scissors":
            return w

    elif u == "paper":
        if c == "scissors":
            return l
        elif c == "rock":
            return w

    elif u == "scissors":
        if c == "rock":
            return l
        elif c == "paper":
            return w


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
