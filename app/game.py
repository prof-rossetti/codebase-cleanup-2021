
from random import choice

#
# USER SELECTION
#

valid_options = ["rock", "paper", "scissors"]

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in valid_options:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(valid_options)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == c:
    print("You tied.")
elif (u, c) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
    print("You win!")
else:
    print("You lose.")