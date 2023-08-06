# Module 2, Lecture 2, Homework 3

import os

# Write a program that opens a file for reading and handles FileNotFoundError if the file is not found.

file_name = input("Enter the name of the file to open: ")


try:
    f = open(file_name, 'r')
    file_stat = os.stat(file_name)
    file_size = file_stat.st_size
    f.close()

except FileNotFoundError as e:
    print(f"\nFile '{file_name}' does not exist.")

else:
    print(f"Size {file_name}: {file_size} bytes")

print(f"\nProgram that opens a file for reading and handles FileNotFoundError if the file is not found")


