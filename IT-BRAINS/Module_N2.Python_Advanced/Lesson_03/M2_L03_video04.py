class Task:
    def __init__(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = completed

    def print_task(self):
        print(f"Task: {self.title} with status {self.completed}")


title = "Title 1"
description = "Description 1"

task1 = Task("Task 1", "Description for task 1", True)
task2 = task1
task2.title = "Another title"

print(task1.title)
print(task2.title)
# print(task1)
# task1.print_task()

"""
title = "Title 1"
description = "Description 1"
task1 = [1]
task2 = [1]


[1] = {
    title = "Task 1",
    description = "Description"
    completed = True
}
"""


