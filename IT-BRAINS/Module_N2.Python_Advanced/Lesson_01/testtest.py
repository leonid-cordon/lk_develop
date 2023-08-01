import random

"""
This is a word guessing game. The program will randomly select a word from a list of words and the user will have a
limited number of attempts to guess the word by guessing individual letters or the entire word.
"""

# This is the list of words that the program can choose from.
lk_list = ['banana', 'pizza', 'ninja', 'robot', 'zombie', 'cookie', 'monkey', 'guitar', 'magic', 'dragon', 'rainbow',
           'unicorn', 'cheese', 'disco', 'rocket', 'pirate', 'ninja', 'panda', 'sushi', 'smile']

# The program will randomly select one word from the list of words.
lk_word = random.choice(lk_list)
print(lk_word)
lk_word_list = list(lk_word)   # Convert the selected word into a list of characters for easier manipulation.
stars = "*" * len(lk_word)  # Create a string of asterisks with the same length as the selected word.
stars_list = list(stars)  # Convert the string of asterisks into a list of characters for easier manipulation.

# The program will prompt the user to enter the number of attempts they would like to have to guess the word.
string1 = "Guess the word: " + stars
string2 = "Write the number of attempts: "
max_length = max(len(string1), len(string2))

print("Welcome! Try to guess the word!".rjust(max_length))
print(string1.rjust(max_length + len(lk_word)))  # Display the current state of the word being guessed, with asterisks
                                                 # representing unguessed letters.

try_count = 0
while True:
    try:
        try_count = int(input("Write the number of attempts: ".rjust(max_length)))    # Prompt the user to enter
                                                                                       # the number of attempts they
                                                                                       # would like to have.
        break
    except ValueError:
        print("Please enter a valid number for the number of attempts.".rjust(max_length))  # If the user enters an
                                                                                             # invalid value, display an
                                                                                             # error message and prompt
                                                                                             # them again.

print(string1.rjust(max_length + len(lk_word)))  # Display the current state of the word being guessed, with asterisks
                                                 # representing unguessed letters.

# The program will wait for the user to enter a letter or a whole word.
guessed_word = False  # This flag variable is used to track whether or not the user has guessed the word.
attempt = 0
while not guessed_word and attempt < try_count:   # The loop will continue until either the user has guessed the word or
                                                  # they have run out of attempts.
    letter_or_word = input("Write a letter or word: ".lower().rjust(max_length))  # Prompt the user to enter either a
                                                                                   # single letter or an entire word.
    if len(letter_or_word) == 1 and letter_or_word.isalpha():  # If the user entered a single letter...
        if letter_or_word in lk_word:  # ...and that letter is in the selected word...
            for i in range(len(lk_word)):
                if letter_or_word == lk_word_list[i]:  # ...find all occurrences of that letter in the selected word...
                    stars_list[i] = letter_or_word  # ...and replace those occurrences in stars_list with that letter.
            print(f"You guessed the letter: {letter_or_word}".rjust(max_length))  # Inform the user that they have
                                                                                   # correctly guessed a letter.
            string1 = "".join(stars_list)  # Update string1 with the current state of stars_list.
            if string1 == lk_word:  # If all letters in stars_list have been replaced (i.e. there are no more asterisks),
                                    # then...
                print(f"You guessed the word: {lk_word}".rjust(max_length))  # ...inform the user that they have correctly
                                                                             # guessed the entire word...
                guessed_word = True  # ...and set this flag variable to True to indicate that they have won.
                break
            print(string1.rjust(max_length + len(lk_word)))  # Display the current state of stars_list, which represents
                                                             # which letters in lk_word have been correctly guessed by
                                                             # replacing asterisks with those letters.
        else:
            print("There is no such letter ".rjust(max_length))  # If there is no such letter in lk_word, inform
                                                                  #the user and...
            attempt += 1  # ...increment this variable to indicate that one attempt has been used up.
            print(f"You used {attempt} out of {try_count} attempts.".rjust(max_length))  # Display the number of
                                                                                          # remaining attempts.
            print(string1.rjust(max_length + len(lk_word)))  # Display the current state of stars_list, which represents
                                                             # which letters in lk_word have been correctly guessed by
                                                             # replacing asterisks with those letters.
    else:  # If more than one character was entered...
        if letter_or_word == lk_word: # ...compare it to lk_word...
            print(f"You guessed the word: {lk_word}".rjust(max_length))  # ...and if it is the same, inform the user that
                                                                         # they have correctly guessed the entire word...
            guessed_word = True  # ...and set this flag variable to True to indicate that they have won.
            break
        else:
            print("Please enter a single letter or the full word.")  # If the entered word is not the same as lk_word,
                                                                      # inform the user and prompt them again.
else:
    if not guessed_word:  # If this flag variable is still False after the loop has finished, then...
        print(f"You didn't guess the word: {lk_word}".rjust(max_length))  # ...inform the user that they have lost and
                                                                          # display the word that they were trying to guess.