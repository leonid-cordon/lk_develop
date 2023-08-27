# Module 2, Lecture 4, Homework 5
# Create a decorator named retry that takes the number of attempts as its
# first argument. This decorator is used to repeat the execution of a
# function in case it raises an error.

def retry(attempts):
    """
    Decorator that repeats the execution of a function in case of an error.
    Args:
        attempts (int): Number of attempts to retry the function.

    Returns:
        function: Decorator function.

    Raises:
        Exception: Raised when the function fails after all the attempts.

    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(attempts):
                try:
                    num = int(input("Enter a number: "))
                    result = func(num, **kwargs)
                    return result
                except ValueError:
                    print("Invalid input. Retry...")
            raise Exception(f"Function {func.__name__} was not executed after {attempts} attempts.")

        return wrapper

    return decorator


@retry(3)
def lk_sum(num1: int):
    print(f"sum(range({num1:,})) = {sum(range(num1)):,}")


lk_sum()



