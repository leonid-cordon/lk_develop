# Module 2, Lecture 1, Homework 1
# Handle an IndexError exception when an application tries to access the wrong index in a list.

lk_list = [00, 11, 22, 33, 44, 55, 66, 77, 88]
lk_ind = int(input("Write an index from 0 to 8 or 9: "))

# Try to access the element at the specified index
try:
    value_at_index = lk_list[lk_ind]
except IndexError as e_ie:
    # If an IndexError occurs, print the error message and the invalid index
    print("Error:", e_ie)
    print("The list does not have an element at index ", lk_ind)
else:
    # If no exception occurs, print the value at the specified index
    print("Value at index {} is: {}".format(lk_ind, value_at_index))

