# Module 2, Lecture 7, Homework 1
# Write a recursive function that calculates the sum of digits of a given number.

def sum_digits(integer: int) -> int:
    """
    Recursive function to calculate the sum of digits of a given number.
    """
    string_ = str(integer)
    n = len(string_)

    if n == 1:  # Base case: if the number has only one digit
        return int(string_)  # Return the digit as the sum

    else:  # Recursive case: if the number has more than one digit
        sum_number = int(string_[n - 1]) + sum_digits(
            int(string_[:n - 1]))  # Calculate the sum of the last digit and the sum of remaining digits
    return sum_number  # Return the total sum


print(sum_digits(1234))  # Output: 10


# def sum_digits(number: int) -> int:
#     if number < 10:  # Base case: if the number has only one digit
#         return number  # Return the number as the sum
#
#     else:  # Recursive case: if the number has more than one digit
#         last_digit = number % 10  # Get the last digit of the number
#         remaining_digits = number // 10  # Get the remaining digits of the number
#         return last_digit + sum_digits(
#             remaining_digits)  # Calculate the sum of the last digit and the sum of remaining digits
#
#
# print(sum_digits(1234))   # Output: 10
