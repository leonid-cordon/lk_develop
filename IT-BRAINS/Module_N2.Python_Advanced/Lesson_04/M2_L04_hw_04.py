# Module 2, Lecture 4, Homework 4
# Implement the timeit decorator that measures the execution time of
# the decorated function and prints it. To obtain the execution time,
# use the time module and the time.time() function.

from time import time


def time_it(func):
    def wrapper(*args, **kwargs):
        print("First line")
        start_time = time()
        func(*args, **kwargs)
        print("Last line")
        elapsed_time = time() - start_time
        print(f"elapsed_time = {elapsed_time}")

    return wrapper


@time_it
def lk_sum(num1: int):
    print(f"sum(range({num1:,})) = {sum(range(num1)):,}")
    # sum(range(30 000 000)) = 449,999,985,000,000


lk_sum(30000000)