# Module 2, Lecture 6, Homework 1
# Write a class "Person" that has properties name and age. Make these
# properties private so that they cannot be directly modified from outside
# the class.
# Provide methods for accessing these properties and setting their values.
class Person:
    def __init__(self):
        """
        Initializes a new instance of the Person class with empty name and age.
        """
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person()
person.set_name("John")
person.set_age(25)
print(person.get_name())  # Виведе "John"
print(person.get_age())  # Виведе 25
# print(person._Person__age)


