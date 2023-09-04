# Module 2, Lecture 6, Homework 3
# Develop a class called "Car" that has the following properties:
# make (car make), model (car model), year (year of manufacture),
# and mileage (car mileage). Provide access to these properties through methods,
# and make the "make" and "model" properties private.
#
# Add a "drive" method to the "Car" class that increases the car's mileage by a
# specified value. Check if the mileage exceeds a given limit (e.g., 300,000 miles)
# and display a message indicating the limit has been reached when attempting to
# drive the car.

# Разработайте класс "Car" (Автомобиль), который будет иметь следующие свойства:
# make (марка автомобиля), model (модель автомобиля), year (год выпуска
# автомобиля) и mileage (пробег автомобиля). Обеспечьте доступ к этим свойствам
# через методы, а также сделайте свойства "make" и "model" приватными.
#
# Добавьте метод "drive" (ехать) в класс "Car", который увеличивает пробег
# автомобиля на определенное значение. Проверьте, не превышает ли пробег
# заданный лимит (например, 300 000 км) и выведите сообщение о достижении
# лимита при попытке совершить поездку.

class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def set_make(self, make):
        """Set the make of the car."""
        self.__make = make

    def set_model(self, model):
        """Set the model of the car."""
        self.__model = model

    def set_year(self, year):
        """Set the year of the car."""
        self.year = year

    def set_mileage(self, mileage):
        """Set the mileage of the car."""
        self.mileage = mileage

    def get_make(self):
        """Get the make of the car."""
        return self.__make

    def get_model(self):
        """Get the model of the car."""
        return self.__model

    def get_year(self):
        """Get the year of the car."""
        return self.year

    def get_mileage(self):
        """Get the mileage of the car."""
        return self.mileage

    def drive(self, plus_mileage):
        """Drive the car and increase the mileage."""
        if self.mileage + plus_mileage >= 300000:
            print("Cannot drive this car. Mileage will exceed 300,000 miles.")
        else:
            self.mileage += plus_mileage
            print(f"Increasing mileage by {plus_mileage} miles.")


car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make())  # Prints "Toyota"
print(car.get_model())  # Prints "Camry"
print(car.get_year())  # Prints 2020
print(car.get_mileage())  # Prints 5000
car.drive(100)  # Increasing mileage by 100 miles
print(car.get_mileage())  # Prints 5100
car.drive(300000)  # Prints a message about exceeding the limit
