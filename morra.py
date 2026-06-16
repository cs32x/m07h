### m07/morra.py
"""Command-line Morra: human vs computer."""

WINNING_SCORE = 3
FINGERS_MIN = 1
FINGERS_MAX = 5
GUESS_MIN = 2
GUESS_MAX = 10


def prompt_int(prompt, minimum, maximum):
    """Grab an integer from the user within the given range."""
    
    # INSERT YOUR CODE HERE

    return value


def computer_choice():
    """Pick fingers and a guess at random."""
    
    # INSERT YOUR CODE HERE

    return fingers, guess


def play_round(human_score, computer_score):
    """Play one round and return updated scores."""
    print(f"\n--- Round (You {human_score} - {computer_score} Computer) ---")
    
    # INSERT YOUR CODE HERE

    return human_score, computer_score


def main():
    print("### Welcome to Morra! ###")
    print(f"""
In each round, pick fingers ({FINGERS_MIN}-{FINGERS_MAX}) and your guess for the
combined total ({GUESS_MIN}-{GUESS_MAX}). The first player to {WINNING_SCORE} points wins.""")

    human_score = 0
    computer_score = 0

    while human_score < WINNING_SCORE and computer_score < WINNING_SCORE:
        human_score, computer_score = play_round(human_score, computer_score)

    print("\n=== Game over ===")
    if human_score > computer_score:
        print(f"You win {human_score}-{computer_score}! Congratulations!")
    else:
        print(f"Computer wins {computer_score}-{human_score}. Better luck next time!")


if __name__ == "__main__":
    main()
