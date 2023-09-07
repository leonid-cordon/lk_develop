# Module 2, Lecture 6, Homework 5
# Extend the Rectangle class from the previous task by overriding the display_color() method.
# In the display_color() method, print a message about the color of the rectangle and also include
# a message about its dimensions (width and height)..


class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print("Color:", self.color)


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_color(self):
        print(f"Color: {self.color}, Width: {self.width}, Height: {self.height}")


rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()  # Output: "Color: Blue, Width: 10, Height: 5"

