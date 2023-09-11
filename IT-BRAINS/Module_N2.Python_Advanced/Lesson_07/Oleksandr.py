class NoDunderAttributes(type):
    def __new__(cls, name, bases, class_dict):
        for attr_name in class_dict:
            srez = "_" + name + "__"
            if srez in attr_name:
                raise ValueError('Cannot use attribute names starting with "__"')
        return super().__new__(cls, name, bases, class_dict)


class MyPrivateClass(metaclass=NoDunderAttributes):
    secret_attribute = 10


class MyPrivateClassTwo(metaclass=NoDunderAttributes):
    __secret_attribute_two = 10
    # ValueError: Cannot use attribute names starting with '__'

