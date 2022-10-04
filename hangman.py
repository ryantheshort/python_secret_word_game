import wordlist

# Take a random word from the word list.
def get_word(): 
    word = wordlist.get_random_word()
    return word.upper()

# Add spaces between characters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the display (IF YOU HAVE TIME)
def draw_screen(number_wrong, number_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    draw_hangman(number_wrong)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", number_guesses,
          "  Wrong:", number_wrong,
          "  Tried:", add_spaces(guessed_letters))

# Get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. " +
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

# Input/process/draw technique. Common in game programmng, evidently.

def play_game():
    word = get_word()

    word_length = len(word)
    remaining_letters = word_length
    displayed_word = "_" * word_length

    number_wrong = 0
    number_guesses = 0
    guessed_letters = ""

    draw_screen(number_wrong, number_guesses, guessed_letters, displayed_word)

    while number_wrong < 7 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess

        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters += 1
                else:
                    displayed_word += "_"
        else:
            number_wrong += 1

        number_guesses += 1

        draw_screen(number_wrong, number_guesses, guessed_letters, displayed_word)
    
    print("-" * 79)

    if remaining_letters == 0:
        print("Congratulations! You got it in", number_guesses, "guesses.")
    else:
        print("Sorry, you lost! The word was: ", word)


def main():
    number_of_guesses = 7
    print("Play the H A N G M A N game")
    draw_hangman(number_of_guesses)
    while True:
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ").lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()