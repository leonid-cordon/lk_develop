# Module 2, Lecture 5, Homework 1
# Change the even_odd_generator function to generate a sequence of numbers from 1 to n with the strings
# "Fizz" for numbers divisible by 3, "Buzz" for numbers divisible by 5, and "FizzBuzz" for numbers
# divisible by 3 , and on 5.

def even_odd_generator(num):
    """
    Generates a sequence of numbers from 1 to n with replacements of 'Fizz', 'Buzz', and 'FizzBuzz'
    based on divisibility rules.

    Args:
        num (int): The upper limit of the number sequence (inclusive).

    Yields:
        str or int: The next number in the sequence or its replacement ('Fizz', 'Buzz', or 'FizzBuzz').

    """
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i


for el in even_odd_generator(15):
    print(el)


# def even_odd_generator(num: int):
#     i = 1
#     while i <= num:
#         if i % 3 == 0 and i % 5 == 0:
#             yield "FizzBuzz"
#         elif i % 3 == 0:
#             yield "Fizz"
#         elif i % 5 == 0:
#             yield "Buzz"
#         else:
#             yield i
#         i += 1
#
#
# for el in even_odd_generator(15):
#     print(el)

