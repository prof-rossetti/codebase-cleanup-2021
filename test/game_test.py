
# TODO: import some code
from app.game import determine_winner

# TODO: test the code
def test_determine_winner():
    #The first entry is the user choice, the second in the computer choice

    # If User Choice is Rock
    assert determine_winner("rock" , "rock") == "None"
    assert determine_winner("rock", "paper") == "Computer"
    assert determine_winner("rock", "scissors") == "User"

    # If User Choice is Paper
    assert determine_winner("paper" ,"rock") == "User"
    assert determine_winner("paper", "paper") == "None"
    assert determine_winner("paper", "scissors") == "Computer"

     # If User Choice is Scissors
    assert determine_winner("scissors" ,"rock") == "Computer"
    assert determine_winner("scissors", "paper") == "User"
    assert determine_winner("scissors", "scissors") == "None"