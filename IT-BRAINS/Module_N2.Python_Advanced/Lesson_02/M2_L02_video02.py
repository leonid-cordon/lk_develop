import os

# video01
# f = open ("files/example.txt", "r") # relative path
#
# # "r"- default  "w"
# print(f.read()) # often this read
# print(f.read(100))  # 100 bytes
# print(f.read(100))  # 100 bytes  next
# f.seek(0)  # carriage return
# f.close() # Explicitly always close the file

#
# filename = "example.txt"
# f = open(filename)
# print(f.read())
# f.close()

# abs_path = os.path.abspath(__file__)
# print(abs_path)


# base_dir = os.path.dirname(abs_path)
# print(abs_path)
#
# file_path = base_dir + '/' + filename  #  в разных ОС разные слеши и т.д.
#
# file_path = os.path.join(base_dir, "file_dir", filename)
# concatenation - конкатенация - укр конкатенація -
# print(file_path)

# video02
abs_path = os.path.abspath(__file__)
filename = "example.txt"
base_dir = os.path.dirname(abs_path)
print(base_dir)
file_path = os.path.join(base_dir, "dir02", filename)
f = open(file_path)
print(f.read())
f.close()

