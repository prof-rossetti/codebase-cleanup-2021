
from random import choice

#
# USER SELECTION
#
def determine_winner(u, c):
    
    winners = { "rock": "scissors", "scissors": "paper", "paper": "rock"}
    choice2Win = winners[u]

    if (u == c):
        winner = "None"
        print("It's a tie!")
    elif (c == choice2Win):
        winner = "User"
        print("The User Wins!")
    else:
        winner = "Computer"
        print("The Computer Wins!")

    return winner

VALID_OPTIONS = ["rock", "paper", "scissors"]

if __name__ == "__main__":
    
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