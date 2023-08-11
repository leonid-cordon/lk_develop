class Rectangle:
    def __init__(self, lk_a, lk_b):
        self.lk_a = lk_a
        self.lk_b = lk_b

    def set_dimensions(self, lk_a, lk_b):
        self.lk_a = lk_a
        self.lk_b = lk_b

    def get_dimensions(self):
        return self.lk_a, self.lk_b

    def calculate_area(self) -> float:
        return self.lk_a * self.lk_b

    def calculate_perimeter(self) -> float:
        return 2 * (self.lk_a + self.lk_b)

    def __str__(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()
        dimensions = f"Dimensions: {self.lk_a} x {self.lk_b}"
        area_info = f"Area: {area}"
        perimeter_info = f"Perimeter: {perimeter}"
        return f"{dimensions}\n{area_info}\n{perimeter_info}"


rec_red = Rectangle(10, 5)
print(rec_red)
rec_red.set_dimensions(8, 6)
print(rec_red.get_dimensions())
print(f"Area: {rec_red.calculate_area()}")
print(f"Perimeter: {rec_red.calculate_perimeter()}")