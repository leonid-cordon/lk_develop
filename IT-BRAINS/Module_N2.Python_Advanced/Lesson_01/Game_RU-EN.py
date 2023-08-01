import random
import requests

# Set your Yandex.Translate API key here
api_key = "YOUR_API_KEY_HERE"

# Prompt the user to enter a word in Russian
lk_word_russian = input("Enter a word in Russian: ")

# Translate the entered word into English using the Yandex.Translate API
url = f"https://translate.yandex.net/api/v1.5/tr.json/translate?key={api_key}&text={lk_word_russian}&lang=ru-en"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    lk_word = data["text"][0]
else:
    print("Translation failed")
    exit()

# Convert the selected word into a list of characters for easier manipulation
lk_word_list = list(lk_word)

# Create a string of asterisks with the same length as the selected word
stars = "*" * len(lk_word)

# Convert the string of asterisks into a list of characters for easier manipulation
stars_list = list(stars)

# Prompt the user to enter the number of attempts they would like to have to guess the word
string1 = f"Guess the word ({lk_word_russian}): {stars}"
string2 = "Write the number of attempts: "
max_length = max(len(string1), len(string2))

print("Welcome! Try to guess the word!".rjust(max_length))
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
    letter_or_word = input("Write a letter or word: ".lower().rjust(max_length))

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