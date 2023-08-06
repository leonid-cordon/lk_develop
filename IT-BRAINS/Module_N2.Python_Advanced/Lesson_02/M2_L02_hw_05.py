# Module 2, Lecture 2, Homework 5
# import regex module
import re

"""
Write a program that reads the contents of a text file and outputs the number of words in it.
"""

file_name = "example.txt"
f = open(file_name, 'r')
str_file = f.read()
f.close()

print(str_file)

# Count the number of words using regular expression
# \w+ matches one or more word characters
# re.findall returns a list of all matched words
print(len(re.findall(r'\w+', str_file)))

# Hello World! Welcome everyone!
# 4

