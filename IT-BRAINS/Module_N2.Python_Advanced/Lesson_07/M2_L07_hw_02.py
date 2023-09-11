# Module 2, Lecture 7, Homework 2
# Create a metaclass that logs a message to the console when a new class is created.

class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        # Create a new class using the parent class's __new__ method
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        # Print a message when a new class is created
        print(f'Class "{name}" has been created')
        super().__init__(name, bases, attrs)


class MyClass(metaclass=LoggingMeta):
    pass  # Prints: 'Class "MyClass" has been created'

