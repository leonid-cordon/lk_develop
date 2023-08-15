# Module 2, Lecture 3, Homework 6

# Create a class called Circle that represents a circle.
# Implement methods for calculating the area and circumference of the circle.
# Use a class attribute to store the value of π (pi).

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return self.pi * (self.radius ** 2)

    def circle_length(self):
        return 2 * self.pi * self.radius

    def __str__(self):
        return f"Square = {self.square()} and circle length = {self.circle_length()}"


circle_01 = Circle(5)
print(circle_01)


