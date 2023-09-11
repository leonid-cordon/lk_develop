class CamelCase(type):
    def __new__(cls, name, bases, class_dict):
        if name[0].upper() != name[0]:
            error_message_ = f"Raises error: '{name}' class name not in CamelCase"
            raise ValueError(error_message_)
        return super().__new__(cls, name, bases, class_dict)


try:
    class NotCamelCase2(metaclass=CamelCase):
        pass  # Raises error: 'Class name not in CamelCase'
except ValueError as e:
    error_message = str(e)
    error_message = error_message[error_message.index("'"):]
    print("Raises error:", error_message)
# class NoDunderAttributes(type):
#     def __new__(cls, name, bases, class_dict):
#         # Проверяем все атрибуты класса на наличие "__" в начале и выбрасываем ошибку при обнаружении
#         # print(class_dict)
#         # print("bases: ", bases)
#         # print("name: ", name)
#         for attr_name in class_dict:
#             print(f"attr_name: {attr_name}")
#             # if attr_name.startswith("__") and not attr_name.endswith("__"):
#             #     raise AttributeError(f'Cannot have attribute names starting with "__"')
#             # print(attr_name)
#             # print(attr_name[:2])
#             # if attr_name[:2] == "__" and attr_name not in ("__module__", "__qualname__"):
#             # print(attr_name, "_" + name + "__" "")
#             srez = "_" + name + "__"
#             if srez in attr_name:
#                 raise ValueError('Нельзя использовать имена атрибутов, начинающиеся с "__"')
#         return super().__new__(cls, name, bases, class_dict)
#
#
# class MyPrivateClass(metaclass=NoDunderAttributes):
#     secret_attribute = 10  # ValueError: Cannot use attribute names starting with '__'
#
#
# class MyPrivateClassTwo(metaclass=NoDunderAttributes):
#     __secret_attribute_two = 10  # ValueError: Cannot use attribute names starting with '__'
#     # Python автоматически преобразует его в _MyPrivateClassTwo__secret_attribute_two,
#     # чтобы избежать возможных конфликтов с атрибутами других классов.
