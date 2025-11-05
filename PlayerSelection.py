import random
import os
import sys

def clear_screen():
    """Clears the console screen for privacy (works on most systems)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def single_player_game():
    print("\n🎮 Single Player Mode")
    print("I'm thinking of a number between 1 and 50.")
    print("You have 7 attempts to guess it!\n")

    number_to_guess = random.randint(1, 50)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            user_input = input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess (or type 'exit'): ").strip().lower()

            # Allow the player to exit mid-game
            if user_input == 'exit':
                print("👋 Exiting game. Returning to main menu...")
                return

            if not user_input.isdigit():
                print("⚠️ Please enter a valid number between 1 and 50.")
                continue

            guess = int(user_input)
            if not (1 <= guess <= 50):
                print("🚫 Number out of range. Please enter a number between 1 and 50.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 You guessed the number in {attempts} attempts!")
                break

        except KeyboardInterrupt:
            print("\n🛑 Game interrupted. Returning to main menu...")
            return
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return
    else:
        print(f"😢 You're out of attempts! The number was {number_to_guess}.")

def two_player_game():
    print("\n👥 Two Player Mode")
    print("Player 1 will enter a number between 1 and 50.")
    print("Player 2 will have 7 attempts to guess it.\n")

    # Player 1 enters secret number
    while True:
        try:
            secret_input = input("Player 1, enter a number between 1 and 50 (or 'exit' to quit): ").strip().lower()
            if secret_input == 'exit':
                print("👋 Exiting game. Returning to main menu...")
                return

            if not secret_input.isdigit():
                print("⚠️ Please enter a valid number.")
                continue

            number_to_guess = int(secret_input)
            if 1 <= number_to_guess <= 50:
                break
            else:
                print("🚫 Please enter a number between 1 and 50.")
        except KeyboardInterrupt:
            print("\n🛑 Game interrupted. Returning to main menu...")
            return
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return

    # Hide number from Player 2
    clear_screen()
    print("Player 2, it’s your turn to guess!\n")

    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            user_input = input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess (or type 'exit'): ").strip().lower()

            if user_input == 'exit':
                print("👋 Exiting game. Returning to main menu...")
                return

            if not user_input.isdigit():
                print("⚠️ Please enter a valid number.")
                continue

            guess = int(user_input)
            if not (1 <= guess <= 50):
                print("🚫 Number out of range. Please enter a number between 1 and 50.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 Player 2 wins! You guessed it in {attempts} attempts.")
                break
        except KeyboardInterrupt:
            print("\n🛑 Game interrupted. Returning to main menu...")
            return
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return
    else:
        print(f"😢 Player 2 is out of attempts! Player 1’s number was {number_to_guess}.")

def main():
    while True:
        try:
            print("\n===============================")
            print("🎯 NUMBER GUESSING GAME")
            print("===============================")
            print("1. Single Player")
            print("2. Two Player")
            print("3. Quit")

            choice = input("Choose an option (1/2/3): ").strip().lower()

            if choice == '1':
                single_player_game()
            elif choice == '2':
                two_player_game()
            elif choice == '3' or choice == 'exit':
                print("👋 Thanks for playing! Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please choose 1, 2, or 3.")
                continue

            # Ask to play again safely
            while True:
                again = input("\nWould you like to play again? (y/n): ").strip().lower()
                if again in ('y', 'n'):
                    break
                print("⚠️ Please enter 'y' or 'n'.")

            if again != 'y':
                print("👋 Thanks for playing! See you next time.")
                break

        except KeyboardInterrupt:
            print("\n🛑 Game interrupted. Exiting safely...")
            sys.exit()
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print("Restarting the main menu...\n")

if __name__ == "__main__":
    main()
