# Module 2, Lecture 4, Homework 7

#     Декоратор rate_limit ограничивает количество вызовов декорированной функции в течение определенного
# временного периода.
#     Декоратор принимает два параметра: max_calls - максимальное количество разрешенных вызовов функции,
# и period - количество секунд, в рамках которых можно сделать max_calls вызовов.
# Для решения этой задачи нам пригодится модуль datetime.
# import datetime

#    The rate_limit decorator restricts the number of calls to a decorated function within a specific
# time period.
#    The decorator accepts two parameters: max_calls, which represents the maximum allowed number
# of function calls, and period, which specifies the duration in seconds during which the max_calls
# limit applies. To solve this task, we will use the datetime module
from datetime import datetime


def rate_limit(max_calls, period):
    """
    A decorator function that applies rate limiting to the decorated function.

    Args:
        max_calls (int): The maximum number of calls allowed within the specified period.
        period (int): The time period (in seconds) during which the calls are limited.

    Returns:
        function: The decorated function.

    """
    def decorator(func):
        start_time = datetime.now()
        calls_left = max_calls

        def wrapper(num1, *args, **kwargs):
            nonlocal calls_left
            elapsed_time = datetime.now() - start_time
            if calls_left > 0 and elapsed_time.total_seconds() < period:
                result = func(num1, *args, **kwargs)
                calls_left -= 1
                print(f"sum(range({num1:,})) = {result:,}, elapsed time = {elapsed_time.total_seconds()} seconds")
            else:
                if calls_left == 0:
                    print(f"You have used all attempts ({max_calls})")
                else:
                    print(f"You have run out of time ({period} seconds)")
                return None

        return wrapper

    return decorator


@rate_limit(max_calls=5, period=10)
def lk_sum(_num1: int):
    """
    Function that calculates the sum of a range of numbers.
    """
    sum_result = sum(range(_num1))
    return sum_result


while True:
    num = int(input("Write number (or enter 0 to exit): "))
    if num == 0:
        break
    lk_sum(num)