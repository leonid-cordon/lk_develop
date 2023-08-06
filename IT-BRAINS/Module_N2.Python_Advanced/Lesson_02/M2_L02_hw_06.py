# Module 2, Lecture 2, Homework 6
"""
Create a function that takes a string from the user and writes it to a file.
"""


def lk_write_string_to_file(lk_file_name: str):
    """
    Writes a user-input string to a file.

    Parameters:
    lk_file_name (str): The name of the file to write the string to.

    Returns:
    None
    """
    string_input = input("Enter a string: ")
    # Open the file in write mode
    f = open(lk_file_name, 'w')
    # Write the string to the file
    f.write(string_input)
    # Close the file
    f.close()
    print("String successfully written to the file.")

    # Alternative implementation using 'with' statement
    # with open(lk_file_name, 'w') as file:
    #     file.write(string_input)
    # print("String successfully written to the file.")

    # return


file_name = "test_hw06.txt"
lk_write_string_to_file(file_name)