# Module 2, Lecture 5, Homework 8
# Write a generator that produces a sequence of prime numbers.

def prime_generator():
    """
    This generator produces a sequence of prime numbers.
    """
    number = 2
    while True:
        prime_is = True
        for j in range(2, number):
            if number % j == 0:
                prime_is = False
                break
        if prime_is:
            yield number
        number += 1


# Example of calling and outputting the result
prime_gen = prime_generator()
for i in range(3):
    print(next(prime_gen))


def prime_generator2():
    """
    This generator produces a sequence of prime numbers using more efficient methods.
    Efficiency: This method uses a more efficient approach by excluding even numbers and limiting
    the divisor checking to the square root of the number.
    """
    yield 2  # The first prime number

    number = 3  # Start with the first odd number
    while True:
        is_prime = True
        sqrt_num = int(number ** 0.5) + 1
        for j in range(3, sqrt_num, 2):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 2


# Example of calling and outputting the result
prime_gen = prime_generator2()
for i in range(10):
    print(next(prime_gen))
