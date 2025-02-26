import random

def number_guessing_game():
    """A simple number guessing game."""

    print("Welcome to the Number Guessing Game!")
    print("I've chosen a secret number between 1 and 100.")
    print("Try to guess it!")

    secret_number = random.randint(1, 100)
    guesses_left = 7  # You can adjust the number of guesses

    while guesses_left > 0:
        try:
            guess = int(input(f"You have {guesses_left} guesses left. What's your guess? "))
            if not 1 <= guess <= 100:
                print("Please enter a number between 1 and 100.")
                continue  # Don't count this as a guess
                
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {7 - guesses_left +1} tries.")
                return  # End the game
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

            guesses_left -= 1

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"You ran out of guesses. The number was {secret_number}.")


if __name__ == "__main__":
    number_guessing_game()