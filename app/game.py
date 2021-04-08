
from random import choice

#
# USER SELECTION
#

def RPS_winner(choice1,choice2):
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock"
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors"
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None
        }
    }
    winner = winners[choice1][choice2]
    return winner

VALID_OPTIONS = ["rock", "paper", "scissors"]
u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()


c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

champ = RPS_winner(u,c)

if champ == u:
    print("Yay! You won!")
elif champ == c:
    print("Sorry, the computer won.")
elif champ == None:
    print("You tied.")
