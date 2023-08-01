# import os


# filename = "example.txt"
#
# f = open(filename, 'r')
# print(f.readline())
# print(f.readline())
# f.seek(0)
# print(f.readline())
# f.close()

# filename = "example.txt"
#
# f = open(filename, 'r')
# for line in f.readline():
#     print(line)
# f.seek(0)
# f.close()

filename = "example.txt"
f = open(filename, 'r')
for line in f:
    print(line)
f.close()

