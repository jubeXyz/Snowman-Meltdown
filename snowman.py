import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    r"""
      ___
     /___\
     (o o)
     ( : )
     ( : )
    """,

    # Stage 1: Bottom part starts melting
    r"""
      ___
     /___\
     (o o)
     ( : )
    """,

    # Stage 2: Only the head remains
    r"""
      ___
     /___\
     (o o)
    """,

    # Stage 3: Snowman completely melted
    r"""
      ___
     /___\
    """
]


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
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Display the initial game state
    display_game_state(mistakes, secret_word, guessed_letters)

    # Prompt for one guess (logic will be added later)
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()