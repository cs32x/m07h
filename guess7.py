### m07/guess7.py
import random

def main():
    secret = random.randint(1, 100)
    print(f"DEBUG: The secret number is {secret}")

    while True:   # our game loop
        guess = grab_validated_guess()
        print(f"DEBUG: You guessed {guess}")

        # Check guess against the secret
        if guess == secret:
            print('Exactly! You win!')
            break
        elif guess < secret:
            print('Too small!')
        else:
            print('Too big!')

def grab_validated_guess():
    # Grab the player's guess
    while True:
        try:
            guess = int(input('Please input your guess: '))
            return guess
        except ValueError:
            print('Guesses must be an integer. Try again...')

if __name__ == '__main__':
    main()