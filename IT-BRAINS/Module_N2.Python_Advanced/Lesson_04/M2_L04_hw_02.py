# Module 2, Lecture 4, Homework 2

# Create a context manager called DividerContext that
# prints a specified separator symbol before and after executing
# the main code block. Implement the context manager using two approaches:
# using the contextmanager decorator and using a class

from contextlib import contextmanager


@contextmanager
def divider_context(letter: str):
    """
    A context manager that prints a line of 100 characters consisting of the specified letter
    before and after executing the code inside the 'with' block.
    """
    try:
        print(100 * letter)
        yield
    finally:
        print(100 * letter)


with divider_context('o'):
    print("This is inside the context.")


class DividerContext:  # class DividerContext():

    def __init__(self, letter: str):
        """
        Initializes the DividerContext with the specified letter.

        Args:
            letter (str): The letter to be used for printing the line.
        """
        self.letter = letter

    def __enter__(self):
        print(100 * self.letter)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(100 * self.letter)


with DividerContext("="):
    print("This is inside the context.")












