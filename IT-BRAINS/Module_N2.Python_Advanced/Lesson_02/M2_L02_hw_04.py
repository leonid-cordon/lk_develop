# Module 2, Lecture 2, Homework 4
"""
Implement a function that divides two numbers, but raises a `ZeroDivisionError` if the second number is zero.
"""


def lk_div_two_num(lk_x: int, lk_y: int) -> float:
    """
    Divide two numbers.

    Parameters:
        lk_x (int): The first number to be divided (dividend).
        lk_y (int): The second number to divide by (divisor).

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If the `lk_y` (divisor) is zero, this exception is raised.
    """
    try:
        lk_c = lk_x / lk_y
        return lk_c

    except ZeroDivisionError as e_Ze:
        print(e_Ze)


x, b = 9, 0
print(lk_div_two_num(x, b))

x, b = 9, 1.55
print(lk_div_two_num(x, b))

