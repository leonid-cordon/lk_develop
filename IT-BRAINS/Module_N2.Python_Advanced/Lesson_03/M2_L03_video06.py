class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def make_bee(self):
        print("Bee ...")


mitsubishi = Car("mitsubishi", 'black')
mercedes = Car("mercedes", 'white')

# print(mitsubishi.brand)
# print(mercedes.color)
# print(mitsubishi.wheels)

# Car.wheels = 3
mitsubishi.wheels = 5
mitsubishi.w = 99

print(mitsubishi.wheels)
print(mercedes.wheels)
print(mitsubishi.w)

print(mitsubishi.__dict__)
print(Car.__dict__)

mitsubishi.make_bee()      #
Car.make_bee(mitsubishi)   # явно

"""
mitsubishi = [1]
mercedes = [2]
Car = [0]
[1] = {
    brand = "mitsubishi"
    color = "black"
    wheels = 5
    __class__ = [0]
}
[2] = {
    brand = "mercedes"
    color = "white"
    __class__ = [0]
}
[0] = {
    wheels = 3
    make_bee = func 
}
"""