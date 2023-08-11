class Car:
    wheels = 4

    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed

    @classmethod  # Only link to our class/ We only make changes at the class level.
    def change_wheels_number(cls, wheels):
        cls.wheels = wheels

    def print_max_speed_km(self):
        print(f"Max speed for {self.brand} is {self.max_speed}  km/h")

    def print_max_speed_ml(self):
        print(f"Max speed for {self.brand} is {self.km_to_ml(self.max_speed)}  ml/h")

    @staticmethod  # Has no connection to either class or objects
    def km_to_ml(km):
        return round(km * 0.621371, 3)


mitsubishi = Car("mitsubishi", 'black', 200)
mercedes = Car("mercedes", 'white', 210)

mitsubishi.print_max_speed_ml()
print(mitsubishi.km_to_ml(10))
print(Car.km_to_ml(10))

# mitsubishi.print_max_speed_km()
# mitsubishi.print_max_speed_ml()

# print(mitsubishi.brand)

# print(mitsubishi.wheels)
# print(mercedes.wheels)

# mitsubishi.change_wheels_number(5)
# Car.change_wheels_number(6)
# print(mitsubishi.wheels)
# print(mercedes.wheels)

# Car.wheels = 3
# mitsubishi.wheels = 5
# mitsubishi.w = 99

