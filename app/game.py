
from random import choice

valid_options = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    Params:
        choice1 and choice2 are both strings: one of "rock", "paper", or "scissors"
    """
    winners = {
        "rock":{
            "rock": None, # represents a tie
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None, # represents a tie
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None, # represents a tie
        },
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice


if __name__ == "__main__":

    #
    # USER SELECTION
    #

    user_choice = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", user_choice)
    if user_choice not in valid_options:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    computer_choice = choice(valid_options)
    print("COMPUTER CHOICE:", computer_choice)

    #
    # DETERMINATION OF WINNER
    #

    winner = determine_winner(user_choice, computer_choice)
    
    if winner == user_choice:
        print("YOU WON!")
    elif winner == computer_choice:
        print("COMPUTER WON!")
    elif winner == None:
        print("TIE!")