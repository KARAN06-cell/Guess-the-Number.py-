"""
Guess the Number — a simple text-based game.

Game rules:
- The computer picks a random number in a chosen range.
- The player has a limited number of guesses.
- After each guess, the game tells the player if they were
  too high, too low, or correct.
- Conditional statements drive the difficulty selection,
  the win/lose logic, and the hint system.
"""

import random


def choose_difficulty():
    """Ask the player to pick a difficulty and return (max_number, max_attempts)."""
    print("Choose a difficulty level:")
    print("  1. Easy   (1-50,  10 guesses)")
    print("  2. Medium (1-100, 7 guesses)")
    print("  3. Hard   (1-200, 6 guesses)")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        return 50, 10
    elif choice == "2":
        return 100, 7
    elif choice == "3":
        return 200, 6
    else:
        # Default to Medium if the input isn't recognized
        print("Unrecognized choice — defaulting to Medium.")
        return 100, 7


def get_guess(max_number):
    """Prompt the player until they enter a valid integer guess."""
    while True:
        raw = input(f"Enter your guess (1-{max_number}): ").strip()
        if raw.isdigit():
            guess = int(raw)
            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"Please enter a number between 1 and {max_number}.")
        else:
            print("That's not a valid whole number. Try again.")


def play_round(max_number, max_attempts):
    """Run a single round of the guessing game. Returns True if the player won."""
    secret_number = random.randint(1, max_number)
    attempts_used = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} guesses. Good luck!\n")

    while attempts_used < max_attempts:
        guess = get_guess(max_number)
        attempts_used += 1
        remaining = max_attempts - attempts_used

        if guess == secret_number:
            print(f"\n🎉 Correct! The number was {secret_number}.")
            print(f"You got it in {attempts_used} guess(es).")
            return True
        elif guess < secret_number:
            # Extra hint for "close" guesses
            if secret_number - guess <= 5:
                print("Too low — but you're very close!")
            else:
                print("Too low.")
        else:
            if guess - secret_number <= 5:
                print("Too high — but you're very close!")
            else:
                print("Too high.")

        if remaining > 0:
            print(f"Guesses remaining: {remaining}\n")
        else:
            print(f"\n💀 Out of guesses! The number was {secret_number}.")

    return False


def main():
    print("=" * 40)
    print("      WELCOME TO GUESS THE NUMBER")
    print("=" * 40)

    total_wins = 0
    total_rounds = 0

    while True:
        max_number, max_attempts = choose_difficulty()
        won = play_round(max_number, max_attempts)

        total_rounds += 1
        if won:
            total_wins += 1

        print(f"\nScore so far: {total_wins} win(s) out of {total_rounds} round(s).")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
