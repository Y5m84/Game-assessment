import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("You have 7 attempts to guess it!")

    number_to_guess = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"😢 Sorry, you're out of attempts! The number was {number_to_guess}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
