# Module 2, Lecture 4, Homework 6
# Реалізувати декоратор кешування memoize, який кешує результати декорованої функції
# для покращення продуктивності при повторних викликах з тими самими аргументами.
# Тобто він повинен запамʼятовувати аргументи з якими функція визивалась
# і результат роботи функції з цими аргументами. І у випадку,
# якщо ми вже маємо результат для цих аргументів, просто повернути закешований результат,
# замість виклику функції

# Реализовать декоратор кэширования под названием memoize, который кэширует результаты
# декорированной функции для улучшения производительности при повторных вызовах с теми же
# аргументами. Другими словами, он запоминает аргументы, с которыми вызывалась функция,
# и результат работы функции с этими аргументами. И если у нас уже есть результат для этих
# аргументов, мы просто возвращаем закэшированный результат, вместо вызова функции.

# Implemented a caching decorator called memoize, which caches the results of the decorated
# function to improve performance for repeated calls with the same arguments. In other words,
# it remembers the arguments with which the function was called and the result of the function's
# execution with those arguments. And if we already have a result for those arguments, we simply
# return the cached result instead of calling the function.
from time import time


def memoize(func):
    """
    Decorator function that caches the result of the decorated function.
    """
    lk_cache_num1 = {30000000: 449999985000000,}

    def wrapper(num1: int, *args, **kwargs):
        """
        Wrapper function that wraps the original function and provides caching functionality.
        """
        start_time = time()
        if num1 not in lk_cache_num1:
            # If the result is not in cache, calculate it using the decorated function
            result = func(num1, *args, **kwargs)
            lk_cache_num1[num1] = result
            elapsed_time = time() - start_time
        else:
            # If the result is in cache, retrieve it from there
            result = lk_cache_num1[num1]
            elapsed_time = time() - start_time
        # Print the result and elapsed time
        print(f"sum(range({num1:,})) = {result:,} elapsed time = {elapsed_time}")
        # return result

    return wrapper


@memoize
def lk_sum(_num1: int):
    """
    Function that calculates the sum of a range of numbers.
    """
    sum_result = sum(range(_num1))
    # print(f"sum(range({num1:,})) = {sum_result:,}")
    return sum_result


for _ in range(10):
    print("\n")
    num = int(input("Write number: "))
    lk_sum(num)
