# Module 2, Lecture 2, Homework 7
"""
Implement a program that copies the contents of one file to another.
"""


def lk_copy_file(inp_file: str, out_file: str):
    """
    Copies the contents of one file to another.

    Parameters:
    inp_file (str): The path to the input file.
    out_file (str): The path to the output file.

    Returns:
    None
    """
    f_inp = open(inp_file, "r")
    f_out = open(out_file, "w")
    read_ind = f_inp.read()
    f_out.write(read_ind)
    f_inp.close()
    f_out.close()
    print("File", inp_file, "copied", out_file)

# Alternative implementation using 'with' statement
# def lk_copy_file(inp_file: str, out_file: str):
#     with open(inp_file, "r") as f_inp:
#         with open(out_file, "w") as f_out:
#             read_ind = f_inp.read()
#             f_out.write(read_ind)
#     print("File", inp_file, "copied", out_file)


lk_copy_file("example.txt", "test_hw07.txt")

