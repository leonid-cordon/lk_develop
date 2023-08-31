# Module 2, Lecture 5, Homework 4
# Write a generator that yields a sequence of squares of numbers from 1 to N.


def square_generator(num: int):
    """
    A generator that yields a sequence of squares of numbers from 1 to num.

    :param num: The upper limit (inclusive) for the range of numbers.
    :yield: The square of each number from 1 to num.
    """
    for i in range(1, num + 1):
        yield i ** 2


for square in square_generator(5):
    print(square)

