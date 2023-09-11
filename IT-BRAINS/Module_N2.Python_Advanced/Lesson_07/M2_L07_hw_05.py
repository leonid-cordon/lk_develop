# Module 2, Lecture 7, Homework 5
# Створіть метаклас, який переконується, що назва класу задана у
# форматі CamelCase. Перевірки на те що перший символ заглавний вистачить.

# Создайте метакласс, который убедится, что имя класса задано в формате CamelCase.
# Проверки на то, что первый символ заглавный - будет достаточно.

# Create a metaclass that ensures the class name is in CamelCase format.
# Checking that the first character is uppercase will be sufficient


class CamelCase(type):
    def __new__(cls, name, bases, class_dict):
        if name[0].upper() != name[0]:
            raise ValueError("Class name not in CamelCase")
        return super().__new__(cls, name, bases, class_dict)


class notCamelCase2(metaclass=CamelCase):
    pass  # Raises error: 'Class name not in CamelCase'


class NotCamelCase(metaclass=CamelCase):
    pass
