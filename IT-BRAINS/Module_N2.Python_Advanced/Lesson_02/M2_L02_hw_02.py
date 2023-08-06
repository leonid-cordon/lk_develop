# Module 2, Lecture 2, Homework 2

# Create a function that accepts two numbers from the user and handles an error (и обрабатывает ошибку)
# if the input is not a number.


def lk_get_two_numbers():
    """
    This function prompts the user to enter two numbers and returns them as a tuple.
    If the user enters invalid input (i.e. not a number), the function will print an error message
    and continue to prompt the user until valid input is entered.
    """
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    return num1, num2


# Example usage of the lk_get_two_numbers function
try:
    num01, num02 = lk_get_two_numbers()
    print("Numbers entered:", num01, "and", num02)
    print(f"The sum of {num01} and {num02} is {num01 + num02}")
except KeyboardInterrupt:
    # Handle the case where the user cancels the operation
    print("\nOperation cancelled by the user.")

