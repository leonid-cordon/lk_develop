# # Використання поліморфізму в функціях, які
# # приймають різні типи об'єктів
# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
#
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
#
# def calculate_area_of_shape(shape):
#     return shape.calculate_area()
#
#
# circle = Circle(5)
# rectangle = Rectangle(3, 4)
# print(calculate_area_of_shape(circle))     # Виведе: 78.5
# print(calculate_area_of_shape(rectangle))  # Виведе: 12