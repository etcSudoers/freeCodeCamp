def rock_paper_scissors(player1: str, player2: str) -> str:
    rules = {
        ("Rock", "Scissors"),
        ("Scissors", "Paper"),
        ("Paper", "Rock"),
    }
    if (player1, player2) in rules: matchResult = "Player 1 wins"
    if (player2, player1) in rules: matchResult = "Player 2 wins"
    if player1 == player2: matchResult = "Tie"


    # rules.get((player1, player2)) or rules.get((player2, player1))
    return matchResult

assert rock_paper_scissors("Rock", "Rock") == "Tie"
assert rock_paper_scissors("Rock", "Paper") == "Player 2 wins"
assert rock_paper_scissors("Scissors", "Paper") == "Player 1 wins"
assert rock_paper_scissors("Rock", "Scissors") == "Player 1 wins"
assert rock_paper_scissors("Scissors", "Scissors") == "Tie"
assert rock_paper_scissors("Scissors", "Rock") == "Player 2 wins"

'''

    The input strings will always be "Rock", "Paper", or "Scissors".
    "Rock" beats "Scissors".
    "Paper" beats "Rock".
    "Scissors" beats "Paper".

Return:

    "Player 1 wins" if Player 1 wins.
    "Player 2 wins" if Player 2 wins.
    "Tie" if both players choose the same option.
'''