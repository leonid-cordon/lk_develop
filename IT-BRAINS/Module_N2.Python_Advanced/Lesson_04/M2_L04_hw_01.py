# Module 2, Lecture 4, Homework 1
# Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду.
# Контекстний менеджер повинен виводити час, що минув, при виході з контексту.
# Використовуйте контекстний менеджер для вимірювання часу виконання певного фрагменту коду.
# Реалізувати контекстний менеджер потрібно 2 способами,
# за допомогою декоратора contextmanager та за допомогою класу

# Реализовать менеджер контекста Timer, измеряющий время выполнения блока кода.
# Контекстный менеджер должен выводить прошедшее время при выходе из контекста.
# Используйте контекстный менеджер для измерения времени выполнения определенного фрагмента кода.
# Реализовать контекстный менеджер нужно 2 способами,
# с помощью декоратора contextmanager и с помощью класса

# Implement a Timer context manager that measures the execution time of a code block.
# The context manager should display the elapsed time upon exiting the context.
# Use the context manager to measure the execution time of a specific code fragment.
# The context manager should be implemented in two ways:
#             using the contextmanager decorator and using a class.


from contextlib import contextmanager
from time import time


@contextmanager
def lk_timer():
    try:
        start_time = time()
        yield
    finally:
        end_time = time()
        elapse_time = end_time - start_time
        print(f"Elapsed Time:  {elapse_time}")
        # Elapsed Time:  0.6226418018341064


with lk_timer():
    result = sum(range(30000000))  # 30 million

print(f"sum(range(30 000 000)) = {result:,}")
# sum(range(30 000 000)) = 449,999,985,000,000


class lk_timer_class:
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapse_time = time() - self.start_time
        print(f"\nElapsed Time:  {elapse_time}")
        # Elapsed Time:  0.5931572914123535


with lk_timer_class():
    result = sum(range(30000000))  # 30 million

print(f"Sum(range(30 000 000)) = {result:,}")
# sum(range(30 000 000)) = 449,999,985,000,000

