
from random import choice

#
# USER SELECTION
#
def determine_winner(u, c):
    
  if u == "rock" 
    if (c == "rock"):
        print("It's a tie!")
    if (c == "paper"):
        print("The computer wins")
        break
    if (c == "scissors"):
        print("The user wins")

if u == "paper"
    if (c == "rock"):
        print("The computer wins")
    if (c == "paper"):
        print("It's a tie!")
    if (c == "scissors"):
        print("The user wins")

if u == "scissors"
    if (c == "rock"):
        print("The computer wins")
    if (c == "paper":
        print("The user wins")
    if (c == "scissors"):
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