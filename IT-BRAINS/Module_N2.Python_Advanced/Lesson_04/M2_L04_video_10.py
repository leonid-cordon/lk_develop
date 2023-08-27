# Module 2, Lecture 4, Video 10  -  Приклад створення контекстного менеджера

class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile("example.txt", "a") as f:
    f.write("\n Some other line")


print(f.closed)  # Write Close or no file




