# Module 2, Lecture 2, Homework 8
"""
  Write a program that opens two files for reading and compares their contents,
printing the lines that exist in the first file but are absent in the second.
"""


def lk_compare_files(lk_file_1: str, lk_file_2: str):
    with open(lk_file_1, "r") as f1, open(lk_file_2, "r") as f2:
        content_1 = set(f1.readlines())
        content_2 = set(f2.readlines())

        unique_strings = content_1 - content_2
        for line in unique_strings:
            print(line.strip())


lk_compare_files("file_first.txt", "file_second.txt")



