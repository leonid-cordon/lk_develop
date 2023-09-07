# Module 2, Lecture 6, Homework 7
# Розробіть клас "Square", який успадковує властивості і методи з класу "Rectangle".
# Додайте властивість side_length (довжина сторони) і перевизначте методи, які використовують
# властивості width і height класу "Rectangle", щоб вони використовували властивість side_length
# класу "Square". Виведіть значення ширини, висоти і довжини сторони для об'єкта класу "Square".

# Разработайте класс "Square", который наследует свойства и методы из класса "Rectangle".
# Добавьте свойство side_length (длина стороны) и переопределите методы, которые используют
# свойства width и height класса "Rectangle", чтобы они использовали свойство side_length
# класса "Square". Выведите значения ширины, высоты и длины стороны для объекта класса "Square"

# Develop a class "Square" that inherits properties and methods from the class "Rectangle".
# Add the property "side_length" and override the methods that use the properties "width"
# and "height" of the "Rectangle" class to use the "side_length" property of the "Square" class.
# Display the values of width, height, and side_length for an object of the "Square" class.

class Rectangle:  # Прямоугольник
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color


class Square(Rectangle):  # Square(Квадрат)
    def __init__(self, color, side_length):
        """
          The line super().__init__(side_length, side_length, color)
        initializes the parent class Rectangle with the given arguments.
        """
        super().__init__(side_length, side_length, color)
        self.side_length = side_length

    def display_color(self):
        print("Color:", self.color)


square = Square("Green", 8)
square.display_color()  # Виведе "Color: Green"
print(square.width)  # Виведе 8
print(square.height)  # Виведе 8
print(square.side_length)  # Виведе 8
