# Module 2, Lecture 6, Homework 8
# Опис: Ви розробляєте програму для автосалону, яка обробляє інформацію про
# різні автомобілі. У вас є базовий абстрактний клас Car (автомобіль), який містить
# загальну інформацію про автомобіль, таку як марка та модель. У додаткових
# класах, які успадковують від Car , ви розширюєте функціональність для конкретних
# типів автомобілів.
# 1. Клас Sedan (седан) успадковує від Car . Він має додатковий атрибут - кількість
# дверей.
# 2. Клас SUV успадковує від Car . Він має додатковий атрибут - кількість
# пасажирських місць.
# 3. Клас SportsCar (спортивний автомобіль) успадковує від Car . Він має
# додатковий атрибут - максимальна швидкість.
# Завдання: Створіть об'єкти різних класів (седан, позашляховик, спортивний
# автомобіль) і використовуйте їх функціонал. Виведіть інформацію про кожен
# автомобіль, включаючи загальну інформацію з Car та специфічну інформацію для
# кожного класу.

"""
   Description: You are developing a program for a car dealership that processes
information about different cars. You have a base abstract class called Car,
which contains general information about a car, such as the make and model.
In additional classes that inherit from Car, you extend the functionality
for specific types of cars.

The Sedan class inherits from Car. It has an additional attribute - the number of doors.
The SUV class inherits from Car. It has an additional attribute - the number of passenger seats.
The SportsCar class inherits from Car. It has an additional attribute - the maximum speed.

Task: Create objects of different classes (sedan, SUV, sports car) and use their functionality.
Display information about each car, including the general information from Car and specific
information for each class.

Описание:
 Вы разрабатываете программу для автосалона, которая обрабатывает информацию о различных
автомобилях. У вас есть базовый абстрактный класс Car (автомобиль), который содержит общую информацию
о автомобиле, такую как марка и модель. В дополнительных классах, которые наследуются от Car,
вы расширяете функциональность для конкретных типов автомобилей.

Класс Sedan (седан) наследуется от Car. Он имеет дополнительный атрибут - количество дверей.
Класс SUV наследуется от Car. Он имеет дополнительный атрибут - количество пассажирских мест.
Класс SportsCar (спортивный автомобиль) наследуется от Car. Он имеет дополнительный атрибут
    - максимальная скорость.
  Задание: Создайте объекты разных классов (седан, внедорожник, спортивный автомобиль)
и используйте их функционал. Выведите информацию о каждом автомобиле, включая общую информацию из Car и специфическую информацию для каждого класса.
"""
from abc import abstractmethod


class Car:

    @abstractmethod
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print("Car:", self.make, self.model)


class Sedan(Car):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print("Doors:", self.number_of_doors)


class SUV(Car):
    def __init__(self, make, model, number_passenger_seats):
        super().__init__(make, model)
        self.number_passenger_seats = number_passenger_seats

    def display_info(self):
        super().display_info()
        print("Seats:", self.number_passenger_seats)


class SportsCar(Car):
    def __init__(self, make, model, maximum_speed):
        super().__init__(make, model)
        self.maximum_speed = maximum_speed

    def display_info(self):
        super().display_info()
        print("Max Speed", self.maximum_speed)


# Створюємо об'єкти різних класів
sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)
# Виводимо інформацію про кожен автомобіль
sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()

# # Очікуваний вивід:
# Car: Toyota Camry
# Doors: 4
# -------------------------
# Car: Ford Explorer
# Seats: 7
# -------------------------
# Car: Ferrari 488 GTB
# Max Speed: 330 km/h
