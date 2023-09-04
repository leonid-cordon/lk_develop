# Module 2, Lecture 6, Homework 2
# Розширте клас "Person" з попереднього завдання, додавши методи для зміни
# значень імені та віку. Зробіть так, щоб ім'я не могло містити цифр, а вік був
# обмежений в діапазоні від 0 до 120. При спробі встановити недійсне значення,
# виведіть повідомлення про помилку.

# Расширьте класс "Person" из предыдущего задания, добавив методы для изменения
# значений имени и возраста. Сделайте так, чтобы имя не могло содержать цифры,
# а возраст был ограничен в диапазоне от 0 до 120. При попытке установить
# недопустимое значение, выведите сообщение об ошибке.

# Extend the "Person" class from the previous task by adding methods to modify
# the name and age values. Ensure that the name cannot contain digits, and the
# age is limited to the range from 0 to 120. When attempting to set an invalid
# value, display an error message.

class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        if not any(char.isdigit() for char in name):  # Проверка на отсутствие цифр в имени
            self.__name = name
        else:
            print(f"{name} - Invalid name. Name should not contain digits.")

    def set_age(self, age):
        if age < 121:
            self.__age = age
        else:
            print(f"{age} - Invalid age > 120")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person()
person.set_name("John")
person.set_age(25)
print(person.get_name())  # Виведе "John"
print(person.get_age())  # Виведе 25
person.set_name("John123")  # Виведе повідомлення про помилку
person.set_age(150) # Виведе повідомлення про помилку
