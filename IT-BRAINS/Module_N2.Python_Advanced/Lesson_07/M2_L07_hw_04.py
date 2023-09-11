# Module 2, Lecture 7, Homework 4
# Створіть метаклас, який викидає помилку при спробі створити
# клас з атрибутами, що починаються з '__' (два нижніх підкреслення).

# Create a metaclass that raises an error when attempting to create
# a class with attributes starting with '__' (double underscore).


class NoDunderAttributes(type):
    def __new__(cls, name, bases, class_dict):
        # attr_name: __module__, __qualname__,_MyPrivateClassTwo__secret_attribute_two
        for attr_name in class_dict:
            # Python автоматически преобразует __secret_attribute_two
            # в _MyPrivateClassTwo__secret_attribute_two,
            # чтобы избежать возможных конфликтов с атрибутами других классов.
            srez = "_" + name + "__"  # attr_name: _MyPrivateClassTwo__secret_attribute_two
            if srez in attr_name:
                raise ValueError('Cannot use attribute names starting with "__"')
        return super().__new__(cls, name, bases, class_dict)


class MyPrivateClass(metaclass=NoDunderAttributes):
    secret_attribute = 10


class MyPrivateClassTwo(metaclass=NoDunderAttributes):
    __secret_attribute_two = 10
    # ValueError: Cannot use attribute names starting with '__'



