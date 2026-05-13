import random

# Predefined words
words = ["ALPHA", "Python", "SSCCS", "Intern", "Game"]

# Randomly select a word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:
    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check guess
    if guess in word:
        print("Correct Guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong Guess!")
        wrong_guesses += 1
        print("Remaining chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\n❌ Game Over!")
    print("The correct word was:", word)
