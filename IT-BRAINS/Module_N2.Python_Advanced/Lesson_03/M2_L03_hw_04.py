# Module 2, Lecture 3, Homework 4
# Create a class called Student to represent a student.
# Add attributes such as name, surname, and a list of grades.
# Implement the __len__ method that returns the number of grades for the student.
# Create a list of students and sort it by the number of grades.
class Student:
    """Represents a student."""

    def __init__(self, name, nickname, list_of_grades):
        """
        Initialize a new Student object.

        Args:
            name (str): The name of the student.
            nickname (str): The nickname of the student.
            list_of_grades (list): A list of grades for the student.
        """
        self.name = name
        self.nickname = nickname
        self.list_of_grades = list_of_grades

    def __len__(self):
        """
        Get the number of grades for the student.

        Returns:
            int: The number of grades.
        """
        return len(self.list_of_grades)

    def __lt__(self, other):
        """
        Compare two students based on the number of grades.

        Args:
            other (Student): The other student to compare.

        Returns:
            bool: True if the current student has fewer grades than the other student, False otherwise.
        """
        return len(self) < len(other)

    def __repr__(self):
        """
        Get a string representation of the student.

        Returns:
            str: The string representation of the student.
        """
        return f"Student(name={self.name}, nickname={self.nickname}, list_of_grades={self.list_of_grades})"
# stud_01 = Student(name="Leonid", nickname="Kadantsev", list_of_grades=[4, 5, 4, 5, 5, 3, 4])
# stud_02 = Student(name="Leonid", nickname="Efremov", list_of_grades=[4, 5, 4, 5, 3])
# stud_03 = Student(name="Nikita", nickname="Kadantsev", list_of_grades=[4, 5, 4, 5, 3, 2])
# stud_04 = Student(name="Olena", nickname="Kazhan", list_of_grades=[4, 5, 4, 5, 3, 2, 4])
# students = [stud_01, stud_02, stud_03, stud_04]


students = [
    Student(name="Leonid", nickname="Kadantsev", list_of_grades=[4, 5, 4, 5, 5, 3, 4]),
    Student(name="Leonid", nickname="Efremov", list_of_grades=[4, 5, 4, 5, 3]),
    Student(name="Nikita", nickname="Kadantsev", list_of_grades=[4, 5, 4, 5, 3, 2]),
    Student(name="Olena", nickname="Kazhan", list_of_grades=[4, 5, 4, 5, 3, 2, 4])
]
# Sort students based on the number of grades (ascending order)
sorted_students = sorted(students)
for student in sorted_students:
    print(student)

# Sort students based on the number of grades (descending order)
students.sort(key=lambda student_: len(student.list_of_grades), reverse=True)
for student in students:
    print(student)

