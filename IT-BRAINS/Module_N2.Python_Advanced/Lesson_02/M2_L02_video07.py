# a = {"name": "Vlad"}
# age = input("Enter your age: ")
#
# try:
#     name = a["name"]
# except KeyError as e:
#     print(e)
#     name = "Default"


# try:
#     age = int(age) + 1
#     print("Code after exception")
# except ValueError as e:
#     print(e)
#     age = 18
# except Exception as exception:
#     print(exception, type(exception))
#
# print(f'Hello, {name}.  Yur age is {age}')

# a = {"name": "Vlad"}
#
# try:
#     name = a["name"]
#     surname = a["surname"]
# except KeyError as e:
#     print(e)
#     name = "Default"
#     surname = "Default"
# finally:
#     print("Will execute anyway")  # обязательно выполняется эьтот кот независимо будет исключение или нет


# f = open('example.txt', 'r')
#
#
# try:
#     print(f.readline())
# except Exception as e:
#     print(e, type(e))
# finally:
#     f.close()   # 100% close file !!!!!!!!!!!
#     print("Will execute anyway")  # обязательно выполняется эьтот кот независимо будет исключение или нет
#


age = input()


try:
    age = int(age)
except Exception as e:
    age = 18
finally:
    print(age +18)  # обязательно выполняется эьтот кот независимо будет исключение или нет

