# percent = input("Enter percent between 0 and 100: ")
#
# try:
#     percent = int(percent)
#     if percent > 100 or percent < 0:
#         print("Invalid percent")
# except ValueError as e:
#     percent = 0
#     print(e)
# except Exception as e:
#     print(e)


# percent = input("Enter percent between 0 and 100: ")
#
# # try:
# percent = int(percent)
# if percent > 100 or percent < 0:
#     raise Exception("Invalid percent")
# # except ValueError as e:
# #     percent = 0
# #     print(e)
# # except Exception as e:
# #     print(e)

# output
# Enter percent between 0 and 100: ereded
# Traceback (most recent call last):
#   File "D:\Leonid\IT_BRAINS\leonid-cordon\IT-BRAINS\Module_N2.Python_Advanced\Lesson_02\M2_L02_video08.py", line 17, in <module>
#     percent = int(percent)
#               ^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'ereded'
#
# Process finished with exit code 1

percent = input("Enter percent between 0 and 100: ")

try:
    percent = int(percent)
    if percent > 100 or percent < 0:
        raise Exception("Invalid percent")
except ValueError as e:
    percent = 0
    print(e)
except Exception as e:
    print(e)

    # output
    # C:\Users\PC\AppData\Local\Programs\Python\Python311\python.exe
    # D:\Leonid\IT_BRAINS\leonid - cordon\IT - BRAINS\Module_N2.Python_Advanced\Lesson_02\M2_L02_video08.py
    # Enter
    # percent
    # between
    # 0 and 100: 110
    # Invalid
    # percent
    #
    # Process
    # finished
    # with exit code 0
