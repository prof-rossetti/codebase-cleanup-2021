
# TODO: import some code
from app.game import determine_winner
# TODO: test the code
def test_determine_winner():
    result = determine_winner("rock","rock")
    assert result == "It's a tie!"
