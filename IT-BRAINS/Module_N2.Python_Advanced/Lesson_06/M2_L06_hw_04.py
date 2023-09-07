# Module 2, Lecture 6, Homework 4
# Створіть базовий клас "Shape" (фігура), який має властивість color (колір)
# і метод display_color() для виведення коліру фігури. Створіть похідний клас
# "Rectangle" (прямокутник), який наслідує властивість color і додає властивості
# width (ширина) і height (висота). Забезпечте можливість встановлення значень
# ширини і висоти прямокутника та виведення їх значень

# Создайте базовый класс "Shape" (фигура), который имеет свойство color (цвет)
# и метод display_color() для вывода цвета фигуры. Создайте производный класс
# "Rectangle" (прямоугольник), который наследует свойство color и добавляет
# свойства width (ширина) и height (высота). Обеспечьте возможность установки
# значений ширины и высоты прямоугольника и вывода их значений.

# Create a base class called "Shape" that has a property called color and a
# method called display_color() to display the color of the shape. Create a
# derived class called "Rectangle" that inherits the color property and adds
# properties for width and height. Provide the ability to set the width and
# height values of the rectangle and display their values.


class Shape:
    def __init__(self, color,):
        self.color = color

    def display_color(self):
        print("Color:", self.color)


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height


shape = Shape("Red")
shape.display_color()  # Виведе "Color: Red"
rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()  # Виведе "Color: Blue"
print(rectangle.width)  # Виведе 10
print(rectangle.height)  # Виведе 5
