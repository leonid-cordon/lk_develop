# Module 2, Lecture 4, Homework 3

# Create a simple logging decorator called log_func that will print
# a message before and after calling the decorated function.

def lk_decor(func):
    def wrapper(*args, **kwargs):
        """
        The wrapper function that adds logging behavior.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        """
        print("First line")
        func(*args, **kwargs)
        print("Last line")
    return wrapper


@lk_decor
def lk_sum(num1: int, num2: int):
    print(f"Sum: {num1} + {num2} = {num1 + num2}")


@lk_decor
def lk_multiplication(num1: int, num2: int, num3: int):
    print(f"Multiplication: {num1} * {num2} * {num3} = {num1 * num2 * num3}")


lk_sum(2, 3)
lk_multiplication(3, 4, 5,)



