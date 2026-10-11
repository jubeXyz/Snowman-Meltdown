
import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman and the current word."""
    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check whether every letter has been guessed.
        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman! You win!")
            return

        guess = input("Guess a letter: ").strip().lower()

        # Validate the input.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            mistakes += 1
            print("Wrong guess! The snowman is melting.")

    # Show the final state after the last mistake.
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game over! The word was: {secret_word}")
    print("The snowman melted. Better luck next time!")


if __name__ == "__main__":
    play_game()