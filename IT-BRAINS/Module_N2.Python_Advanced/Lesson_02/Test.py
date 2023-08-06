import os

# Prompt the user to enter the name of the file to open.
file_name = input("Enter the name of the file to open: ")

try:
    # Try to open the file for reading.
    file_handle = open(file_name, 'r')

    # Get file statistics, such as size, using os.stat().
    file_stat = os.stat(file_name)
    file_size = file_stat.st_size

    # Close the file after reading is done.
    file_handle.close()

except FileNotFoundError as e:
    # Handle the case when the file is not found.
    print(f"\nFile '{file_name}' does not exist.")

else:
    # Print the file size in bytes if the file is successfully opened and read.
    print(f"Size of '{file_name}': {file_size} bytes")

print("\nProgram that opens a file for reading and handles FileNotFoundError if the file is not found.")

# In this code:
#
# file_handle.close() - We close the file after reading its contents to free up system resources and avoid potential
# file access conflicts in the future.
#
# else: - This block is executed if there was no exception raised in the try block. It prints the size of the file in
# bytes, which is not checked within the try block.
#
# The code opens a file specified by the user, reads its size, and prints it. If the file does not exist,
# a FileNotFoundError is caught and an appropriate message is displayed.





