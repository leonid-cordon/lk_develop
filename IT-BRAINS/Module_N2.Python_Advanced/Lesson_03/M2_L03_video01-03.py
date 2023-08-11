class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description


task1 = Task("Task 1", "Description 1")
task2 = Task("Task 2", "Description 2")


print(task1.title, task2.title)
print(type(task1))
print(task1)


# class Task:
#     pass
#
#
# task1 = Task()
# task2 = Task()
#
# task1.title = "task 1"
# task1.description = "Description 1"
#
# task2.title = "Task 2"
# task2.description = "Description 2"
#
# print(task1.title)
# print(type(task1))

# class Task:...



# task1 = {
#     "title": "Task 1",
#     "description": "Description for task 1",
#     "completed": True
# }
#
# task2 = {
#     "title": "task 2",
#     "description": "Description for task 2",
#     "completer": False
# }
#
#
# # print(f"Task: {task1['title']} with status {task1['completed']}")
# # print(f"Task: {task2['title']} with status {task2['completed']}")
#
#
# # def print_info(task):
# #     print(f"Task: {task['title']} with status {task['completed']}")
# #
# #
# # print_info(task1)
#
#
# task_1 = Task("Task 1", "Description for task 1", True)
# task_2 = Task("Task 2", "Description for task 2", True)

a = 1