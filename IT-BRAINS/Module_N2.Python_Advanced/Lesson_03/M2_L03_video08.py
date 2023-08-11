class Progress:
    def __init__(self, time, finished_tasks):
        self.time = time
        self.finished_tasks = finished_tasks

    def __add__(self, other):
        return Progress(
            self.time + other.time,
            self.finished_tasks + other.finished_tasks
        )

    def __repr__(self):
        return f"Progress[{self.time}, {self.finished_tasks}]"

    def __str__(self):
        # return self.__repr__()
        return f"Progress({self.time}, {self.finished_tasks})"


p1 = Progress(1, 2)
p2 = Progress(3, 3)
p3 = Progress(2, 1)
p4 = Progress(2, 0)

# result = p1.add(p2).add(p3).add(p4)
result = p1 + p2 + p3 + p4
print(result)
# print(dir(Progress))



