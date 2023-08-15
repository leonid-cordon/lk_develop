# Module 2, Lecture 3, Homework 7

# Create a class called Student that represents a student.
# Implement a class attribute to track the number of students.
# Modify the value of the class attribute in the __init__ method.
# Also, create a class method to display the total number of students.


class Student:

    number_of_students = 0
    # Class attribute to track the number of students

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Student.number_of_students += 1

    def __str__(self):
        return f"Student: {self.name}, {self.surname} - total number of students: {Student.number_of_students}"


student_01 = Student("Leonid", "Kadantsev")
print(student_01)
student_02 = Student("Olena", "Kazhan")
print(student_02)
