# Module 2, Lecture 6, Homework 6
# Опис: Ви розробляєте програму для інформації про тварин в зоопарку. У вас є
# базовий клас Animal (тварина), який містить загальну інформацію про тварину, таку
# як назва та вид. У додаткових класах, які успадковують від Animal , ви розширюєте
# функціональність для конкретних видів тварин.
# 1. Клас Mammal (ссавець) успадковує від Animal . Він має додатковий атрибут - тип
# харчування (наприклад, травоїдний, всеїдний, хижий).
# 2. Клас Carnivore (хижак) успадковує від Mammal . Він має додатковий атрибут -
# кількість зубів.
# 3. Клас Lion (лев) успадковує від Carnivore . Він має додатковий атрибут - розмір
# гриви.
# Завдання: Створіть об'єкти різних класів (лев, хижак, ссавець) і використовуйте їх
# функціонал. Виведіть інформацію про кожну тварину, включаючи загальну
# інформацію з Animal та специфічну інформацію для кожного класу.

# Description: You are developing a program for information about animals in a zoo.
# You have a base class called Animal, which contains general information about the animal,
# such as its name and species. In additional classes that inherit from Animal, you extend
# the functionality for specific types of animals.
#
# The Mammal class inherits from Animal. It has an additional attribute - the type of diet
# (e.g., herbivore, omnivore, carnivore).
# The Carnivore class inherits from Mammal. It has an additional attribute - the number of teeth.
# The Lion class inherits from Carnivore. It has an additional attribute - the size of the mane.
# Task: Create objects of different classes (lion, carnivore, mammal) and utilize their functionality.
# Display information about each animal, including the general information from Animal and
# specific information for each class.

# Описание: Вы разрабатываете программу для информации о животных в зоопарке.
# У вас есть базовый класс Animal (животное), который содержит общую информацию
# о животном, такую как название и вид. В дополнительных классах, которые наследуются
# от Animal, вы расширяете функциональность для конкретных видов животных.
#
# Класс Mammal (млекопитающее) наследует от Animal. Он имеет дополнительный атрибут
# - тип питания (например, травоядное, всеядное, хищное).
# Класс Carnivore (плотоядное) наследует от Mammal. Он имеет дополнительный атрибут
# - количество зубов.
# Класс Lion (лев) наследует от Carnivore. Он имеет дополнительный атрибут - размер гривы.
# Задание: Создайте объекты разных классов (лев, плотоядное, млекопитающее)
# и используйте их функционал. Выведите информацию о каждом животном, включая
# общую информацию из Animal и специфическую информацию для каждого класса.

class Animal:
    def __init__(self, name, species):   # species(вид)
        self.name = name
        self.species = species  # вид

    def display_info(self):
        print("Animal:", self.name)
        print("Species:", self.species)


class Mammal(Animal):  # млекопитающее(Mammal)
    # def __init__(self, name, species, herbivore, omnivore, carnivore, ):
    def __init__(self, name, species, type_diet):
        super().__init__(name, species)
        # тип питания
        self.type_diet = type_diet
        # self.herbivore = herbivore  # травоядное
        # self.omnivore = omnivore  # всеядное
        # self.carnivore = carnivore  # хищное

    def display_info(self):
        super().display_info()
        print("Diet Type:", self.type_diet)

# mammal = Mammal("Elephant", "Mammal", "Herbivore")
# Animal: Elephant
# Species: Mammal
# Diet Type: Herbivore


class Carnivore(Mammal):  # плотоядное животное
    def __init__(self, name, species, type_diet, number_of_teeth):
        super().__init__(name, species, type_diet)
        self.number_of_teeth = number_of_teeth

    def display_info(self):
        super().display_info()
        print("Teeth Count:", self.number_of_teeth)


class Lion(Carnivore):  # хищники
    def __init__(self, name, species, type_diet, number_of_teeth, mane_size):
        super().__init__(name, species, type_diet, number_of_teeth)
        self.mane_size = mane_size

    def display_info(self):
        super().display_info()
        print("Mane Size:", self.mane_size)


# Створюємо об'єкти різних класів
lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

# Виводимо інформацію про кожну тварину
lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()

# Очікуваний вивід:
# Animal: Simba
# Species: Lion
# Diet Type: Carnivore
# Teeth Count: 30
# Mane Size: Large
# -------------------------
# Animal: Tiger
# Species: Carnivore
# Diet Type: Carnivore
# Teeth Count: 40
# -------------------------
# Animal: Elephant
# Species: Mammal
# Diet Type: Herbivore

