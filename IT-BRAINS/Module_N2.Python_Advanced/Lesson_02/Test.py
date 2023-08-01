# Module 2, Lecture 1, Homework 1

"""
Обробіть виняток IndexError, коли програма намагається отримати доступ до неправильного індексу в списку.
Обработайте исключение IndexError, когда приложение пытается получить доступ к неправильному индексу в списке
Handle an IndexError exception when an application tries to access the wrong index in a list.
"""

lk_list = [00, 11, 22, 33, 44, 55, 66, 77, 88]
# print(lk_list)
# print((type(lk_list)))
try:
    lk_ind = int(input("Write an index from 0 to 8 or 9: "))
except ValueError as e_ve:
    print(e_ve)
    print("Index = 0")
    lk_ind = 0

try:
    lk_ind = input(lk_list[lk_ind])
except IndexError as e_ie:
    print(e_ie)
    print(lk_list[8])
else:
    print("Success")