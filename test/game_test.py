
# TODO: import some code
from app.game import determine_winner
# TODO: test the code
def test_determine_winner():
    result = determine_winner("rock","rock")
    assert result == "It's a tie!"
    result = determine_winner("rock","paper")
    assert result == "The user wins"
    result = determine_winner("rock","scissors")
    assert result == "The computer wins"
    result = determine_winner("paper","rock")
    assert result == "The computer wins"
    result = determine_winner("paper","paper")
    assert result == "It's a tie!"
    result = determine_winner("paper","scissors")
    assert result == "The user wins"
    result = determine_winner("scissors","rock")
    assert result == "The user wins"
    result = determine_winner("scissors","paper")
    assert result == "The computer wins"
    result = determine_winner("scissors","scissors")
    assert result == "It's a tie!"
