# Module 2, Lecture 3, Homework 1
# Create a Rectangle class to represent a rectangle. Add methods to calculate area
# and the perimeter of the rectangle. Create a Rectangle object and call these methods
class Rectangle:
    def __init__(self, lk_a, lk_b):
        self.lk_a = lk_a
        self.lk_b = lk_b
        # self.lk_sq = 0

    def lk_square(self) -> float:
        return self.lk_a * self.lk_b
        # self.lk_sq = self.lk_a * self.lk_b
        # return self.lk_sq

    def lk_perimeter(self) -> float:
        return 2 * (self.lk_a + self.lk_b)

    def lk_valid(self):
        if self.lk_a < 0 or self.lk_b < 0:
            raise ValueError("Invalid parameters: dimensions cannot be negative")
            # print("No valid parameters")


rec_red = Rectangle(10, 5)
rec_red.lk_valid()
print(f"Red rectangle are {rec_red.lk_square()}, Perimeter red rectangle {rec_red.lk_perimeter()}")

rec_blue = Rectangle(2.5, 3.8)
rec_blue.lk_valid()
print(f"Blue rectangle are {rec_blue.lk_square()}, Perimeter blue rectangle {rec_blue.lk_perimeter()}")

rec_black = Rectangle(-2, 3.8)
rec_black.lk_valid()
