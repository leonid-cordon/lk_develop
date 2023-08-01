filename = "example.txt"

f = open(filename, 'a+')
f.write("\nHello")
f.seek(0)
print(f.read())


# for line in f:
#     print(line)
f.close()
#
