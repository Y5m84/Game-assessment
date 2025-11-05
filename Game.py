import random
import sys

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("You have 7 attempts to guess it!")
    print("Type 'exit' at any time to quit.\n")

    while True:
        try:
            number_to_guess = random.randint(1, 50)
            attempts = 0
            max_attempts = 7

            while attempts < max_attempts:
                user_input = input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess: ").strip().lower()

                # Exit option
                if user_input == "exit":
                    print("👋 Thanks for playing! Goodbye.")
                    return

                # Check if the input is a number
                if not user_input.isdigit():
                    print("⚠️ Invalid input! Please enter a number between 1 and 50 or type 'exit' to quit.")
                    continue

                guess = int(user_input)

                # Validate the number range
                if not (1 <= guess <= 50):
                    print("🚫 Please enter a number within the range 1 to 50.")
                    continue

                attempts += 1

                # Compare the guess
                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                    break

            else:
                # Only runs if the loop finishes without a correct guess
                print(f"😢 You're out of attempts! The number was {number_to_guess}.")

            # Ask player to play again
            while True:
                play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
                if play_again in ('y', 'n'):
                    break
                else:
                    print("⚠️ Invalid choice. Please type 'y' to continue or 'n' to quit.")

            if play_again != 'y':
                print("👋 Thanks for playing! See you next time.")
                break

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n🛑 Game interrupted by user. Exiting safely...")
            sys.exit()
        except Exception as e:
            # Catch unexpected errors
            print(f"\n❌ An unexpected error occurred: {e}")
            print("Restarting the game safely...\n")

if __name__ == "__main__":
    number_guessing_game()
