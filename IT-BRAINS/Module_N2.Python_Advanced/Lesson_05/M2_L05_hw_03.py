# Module 2, Lecture 5, Homework 3
# Create an iterator that takes a string and each call to
# the next() method will return the next character of the string.

class StringIterator:
    """
    An iterator that takes a string and returns the next character on each call to the 'next()' method.
    """

    def __init__(self, input_string):
        """
        Initializes the StringIterator with the provided input string.

        :param input_string: The string to iterate over.
        """
        self.string = input_string
        self.letter_number = 0
        self.string_length = len(input_string)

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next character from the input string on each call.
        Raises StopIteration when the end of the string is reached.
        """
        if self.letter_number >= self.string_length:
            raise StopIteration
        else:
            letter = self.string[self.letter_number]
            self.letter_number += 1
            return letter


# Example usage and output
string = "Hello, World!"
str_iter = StringIterator(string)
for char in str_iter:
    print(char)


