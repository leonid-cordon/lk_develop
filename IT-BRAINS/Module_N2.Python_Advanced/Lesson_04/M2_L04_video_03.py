# Module 2, Lecture 4, Video 3 - Що таке декоратор, базовий вигляд
# def decorator(func):
#     # патерн
#
#     def inner():
#         print("start")
#         func()
#         print("end")
#
#     return inner
#
#
# @decorator
# def say_hi():
#     print("Hello")
#
#
# @decorator  # синтаксичній сахар
# def say_bye():
#     print("Bye")
#
#
# # say_hi = decorator(say_hi)
# say_hi()
# print(100 * "*")
# # say_bye = decorator(say_bye)
# say_bye()
# ---------------------------------№№№№№№№№№№№№№№
# def decorator(func):
#
#     # патерн
#
#     def inner():
#         print("start")
#         func()
#         print("end")
#
#     return inner
#
#
# def say_hi():
#     print("Hello")
#
# def say_bye():
#     print("Bye")
#
#
# say_hi = decorator(say_hi)
# say_hi()
# print(100*"*")
# say_bye = decorator(say_bye)
# say_bye()


# say_hi()
#
#
# def decorator(func):
#     # патерн
#
#     def inner():
#         print("start")
#         func()
#         print("end")
#
#     return inner
#
#
# def say_hi():
#     print("Hello")
#
#
# decorated_say_hi = decorator(say_hi)
# decorated_say_hi()
# print(100 * "*")
# say_hi()  # сама функция печатается как не в чём не бывало - без изменений

def decorator(func):
    # патерн

    def inner():
        print("start")
        func()
        print("end")

    return inner


def say_hi():
    print("Hello")


# decorated_say_hi = decorator(say_hi)   # @decorator вместо decorator(say_hi)
# decorated_say_hi()
print(100 * "*")
say_hi()