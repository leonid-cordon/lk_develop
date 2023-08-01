# Module 2, Lecture 1, Homework 1

import random

# This program is a word guessing game. The user has a limited number of attempts to guess a randomly selected word.

# List of words for the program to choose from
lk_list = ['banana', 'pizza', 'ninja', 'robot', 'zombie', 'cookie', 'monkey', 'guitar', 'magic', 'dragon', 'rainbow',
           'unicorn', 'cheese', 'disco', 'rocket', 'pirate', 'ninja', 'panda', 'sushi', 'smile']

# Randomly select a word from the list
lk_word = random.choice(lk_list)
# print(lk_word)

# Convert the selected word into a list of characters for easier manipulation
lk_word_list = list(lk_word)

# Create a string of asterisks with the same length as the selected word
stars = "*" * len(lk_word)

# Convert the string of asterisks into a list of characters for easier manipulation
stars_list = list(stars)

# Prompt the user to enter the number of attempts they would like to have to guess the word
string1 = "Guess the word: " + stars
string2 = "Write the number of attempts: "
max_length = max(len(string1), len(string2))

print("Welcome!".rjust(max_length))
print("Try to guess the word!".rjust(max_length))
print(string1.rjust(max_length + len(lk_word)))

try_count = 0
while True:
    try:
        try_count = int(input("Write the number of attempts: ".rjust(max_length)))
        break
    except ValueError:
        print("Please enter a valid number for the number of attempts.".rjust(max_length))

print(string1.rjust(max_length + len(lk_word)))

# Flag variable to track whether or not the user has guessed the word
guessed_word = False

attempt = 0
while not guessed_word and attempt < try_count:
    # Prompt the user to enter either a single letter or an entire word
    letter_or_word = input("Write a letter or word: ".rjust(max_length)).lower()

    # If the user entered a single letter...
    if len(letter_or_word) == 1 and letter_or_word.isalpha():
        # ...and that letter is in the selected word...
        if letter_or_word in lk_word:
            # ...find all occurrences of that letter in the selected word...
            for i in range(len(lk_word)):
                if letter_or_word == lk_word_list[i]:
                    # ...and replace those occurrences in stars_list with that letter.
                    stars_list[i] = letter_or_word

            # Inform the user that they have correctly guessed a letter.
            print(f"You guessed the letter: {letter_or_word}".rjust(max_length))

            # Update string1 with the current state of stars_list.
            string1 = "".join(stars_list)

            # If all letters in stars_list have been replaced (i.e. there are no more asterisks), then...
            if string1 == lk_word:
                # ...inform the user that they have correctly guessed the entire word...
                print(f"You guessed the word: {lk_word}".rjust(max_length))
                # ...and set this flag variable to True to indicate that they have won.
                guessed_word = True
                break

            # Display the current state of stars_list, which represents which letters in lk_word have been correctly
            # guessed by replacing asterisks with those letters.
            print(string1.rjust(max_length + len(lk_word)))
        else:
            # If there is no such letter in lk_word, inform the user and...
            print("There is no such letter ".rjust(max_length))
            # ...increment this variable to indicate that one attempt has been used up.
            attempt += 1

            # Display the number of remaining attempts.
            print(f"You used {attempt} out of {try_count} attempts.".rjust(max_length))

            # Display the current state of stars_list, which represents which letters in lk_word have been correctly
            # guessed by replacing asterisks with those letters.
            print(string1.rjust(max_length + len(lk_word)))
    else:
        # If more than one character was entered...
        if letter_or_word == lk_word:
            # ...and if it is the same as lk_word, inform the user that they have correctly guessed the entire word...
            print(f"You guessed the word: {lk_word}".rjust(max_length))
            # ...and set this flag variable to True to indicate that they have won.
            guessed_word = True
            break
        else:
            # If the entered word is not the same as lk_word, inform the user and prompt them again.
            print("Please enter a single letter or the full word.")

# If this flag variable is still False after the loop has finished, then...
if not guessed_word:
    # ...inform the user that they have lost and display the word that they were trying to guess.
    print(f"You didn't guess the word: {lk_word}".rjust(max_length))
