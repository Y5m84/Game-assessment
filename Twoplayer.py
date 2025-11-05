import os

def clear_screen():
    """Clears the screen for privacy (works on most systems)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def two_player_guessing_game():
    print("🎮 Welcome to the Two-Player Number Guessing Game!")
    print("Player 1 will enter a number between 1 and 50.")
    print("Player 2 will have 7 attempts to guess it.\n")

    # Player 1 enters the secret number
    while True:
        try:
            number_to_guess = int(input("Player 1, enter a number between 1 and 50: "))
            if 1 <= number_to_guess <= 50:
                break
            else:
                print("Please enter a number between 1 and 50.")
        except ValueError:
            print("Please enter a valid number.")

    # Hide the number from Player 2
    clear_screen()
    print("Player 2, it’s your turn to guess!\n")

    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 Player 2 wins! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"😢 Player 2 is out of attempts! Player 1’s number was {number_to_guess}.")

if __name__ == "__main__":
    two_player_guessing_game()
