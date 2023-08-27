# Module 2, Lecture 4, Video 7  - Контекстний менеджер
# try:
#     f = open("example.txt", "a")
#     f.write("\nAnother Line")
# except Exception as e:
#     print(e)
# finally:
#     f.close()


# file_descriptiors = []
# for i in range(1000000):
#     file_descriptiors.append(open("example.txt", "a"))

with open("example.txt", "a") as file:
    file.write("\n Another Line2")


