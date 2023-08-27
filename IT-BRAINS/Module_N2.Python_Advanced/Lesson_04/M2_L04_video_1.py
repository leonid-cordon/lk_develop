# Module 2, Lecture 4, Video 1
def print_message(my_type="hello"):

    def say_hi():
        return "Hellp"

    def say_bye():
        return "Bye"

    if my_type == "hello":
        return say_hi
    return  say_bye()


my_func = print_message()
print(my_func)

# def outer_func():
#
#     def greeter():
#         return "Hi"
#
#     print(greeter())
#
#
# outer_func()

# def say_hi(name="Leonid"):
#     print(f"Hello {name}")
#
#
# say_hi()
# say_hi("Anton")
# say_hi_copy = say_hi
# print("111")
# print(say_hi_copy())
# say_hi_copy()