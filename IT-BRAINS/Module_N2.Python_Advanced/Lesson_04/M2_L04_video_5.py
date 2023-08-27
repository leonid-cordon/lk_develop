# Module 2, Lecture 4, Video 5 - Декоратори для функцій з параметрами
from time import time, sleep


def decorator_1(func):

    def inner(*args, **kwargs):
        print(10*"#")
        start = time()
        func(*args, **kwargs)
        end = time()
        print(10*'#')
        print(f"Function time: {end - start}")

    return inner


@decorator_1
def say_hi(name):
    sleep(1)
    print(f"Hello, {name}")


@decorator_1
def another_hi(a,b,c):
    print(f'Hellp, {a}, {b}, {c}')


say_hi('Leonid')
another_hi(a=1, b=2, c=3)
