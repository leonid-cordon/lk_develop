# Module 2, Lecture 5, Homework 2
# Write a generator that returns a sequence of Fibonacci numbers

def fibonacci_generator():
    """
    Generates a sequence of Fibonacci numbers.

    Yields:
        int: The next Fibonacci number in the sequence.

    """
    fib_0, fib_1 = 0, 1
    while True:
        yield fib_0
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        # fib_2 = fib_1 + fib_0
        # fib_0 = fib_1
        # fib_1 = fib_2


# Example usage and result output
fib_gen = fibonacci_generator()
for i in range(10):
    print(next(fib_gen))


