# a = {"name": "Leonid"}
# age = input("Enter your name")
#
# try:
#     print(a['name'])
#     print(a['surname'])
#     print("Code after exception")
# except KeyError:
#     print("Exception raison")
# except Exception:
#     print("Exception raison")


# a = {"name": "Leonid"}
# age = input("Enter your age")
#
# try:
#     print(f"Hello, {a['name']}. Your age is {int(age) + 1}")
#     print("Code after exception")
# except KeyError:
#     print("Exception raison")
# except ValueError:
#     print(f"Hello, {a['name']}. Your age is 20")
# except Exception:
#     print("Another raison")


# a = {"name": "Leonid"}
# age = input("Enter your age")
#
# try:
#     print(f"Hello, {a['name']}. Your age is {int(age) + 1}")
#     print("Code after exception")
# except (KeyError, ValueError):
#     print("Invalid input")
# except Exception:
#     print("Another raison")

# a = {"name": "Leonid"}
# age = input("Enter your age")
# try:
#     print(f"Hello, {a['name']}. Your age is {int(age) + 1}")
#     print(a['surname'])
#     print("Code after exception")
# except Exception as exception:
#     print(exception, type(exception))


a = {"name": "Leonid"}
age = input("Enter your age")

try:
    name = a['name']
except KeyError as e:
    print(e)
    name = "default"


try:
    age = int(age) + 1
    print("Code after exception")
except ValueError as e:
    print(e)
    age = 18  # "default"
except Exception as exception:
    print(exception, type(exception))

print(f"Hello, {name}. Your age is {age}")

