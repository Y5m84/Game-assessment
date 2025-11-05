import random
import os

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
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"😢 You're out of attempts! The number was {number_to_guess}.")

def two_player_game():
    print("\n👥 Two Player Mode")
    print("Player 1 will enter a number between 1 and 50.")
    print("Player 2 will have 7 attempts to guess it.\n")

    # Player 1 enters secret number
    while True:
        try:
            number_to_guess = int(input("Player 1, enter a number between 1 and 50: "))
            if 1 <= number_to_guess <= 50:
                break
            else:
                print("Please enter a number between 1 and 50.")
        except ValueError:
            print("Please enter a valid number.")

    # Hide number from Player 2
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
                print(f"🎉 Player 2 wins! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"😢 Player 2 is out of attempts! Player 1’s number was {number_to_guess}.")

def main():
    while True:
        print("\n===============================")
        print("🎯 NUMBER GUESSING GAME")
        print("===============================")
        print("1. Single Player")
        print("2. Two Player")
        print("3. Quit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            single_player_game()
        elif choice == '2':
            two_player_game()
        elif choice == '3':
            print("👋 Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        # Ask to play again
        again = input("\nWould you like to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    main()
