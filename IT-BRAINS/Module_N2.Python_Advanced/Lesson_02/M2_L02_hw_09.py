# Module 2, Lecture 2, Homework 9
# Create a function that deletes the specified line from a text file.


def lk_del_line_file(lk_file_name: str, lk_num_line: int):
    """
    Deletes the specified line from a text file.

    Args:
        lk_file_name (str): The name or path of the text file.
        lk_num_line (int): The line number to be deleted.

    Returns:
        None
    """
    with open(lk_file_name, 'r') as file:
        lines = file.readlines()

        if lk_num_line < 1 or lk_num_line > len(lines):
            print("Invalid line number: ", lk_num_line)
            return
        else:
            del lines[lk_num_line - 1]

    with open(lk_file_name, "w") as file:
        file.writelines(lines)

    print("Line successfully deleted")


file_path = "test_file_l09.txt"
line_number = 4
lk_del_line_file(file_path, line_number)

