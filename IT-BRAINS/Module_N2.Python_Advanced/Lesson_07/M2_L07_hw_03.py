# Module 2, Lecture 7, Homework 3
# Write a recursive function that reverses the input string.

def reverse_string(string: str) -> str:
    if len(string) == 0:  # Base case: if the string is empty
        return ""  # Return an empty string
    else:
        # Get the first character of the string
        first_letter = string[0]
        # Get the remaining characters of the string
        remaining_chars = string[1:]
        # Recursively reverse the remaining characters
        reversed_remaining = reverse_string(remaining_chars)
        # Concatenate the reversed remaining characters and the first character
        return reversed_remaining + first_letter


print(reverse_string("Hello"))  # Output: "olleH"
