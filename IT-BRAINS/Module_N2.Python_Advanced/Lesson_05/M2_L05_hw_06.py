# Module 2, Lecture 5, Homework 6
# Write a generator that filters out odd numbers from a given sequence

def even_number_filter(nums: list):
    for num in range(len(nums)):
        if nums[num] % 2 == 0:
            yield nums[num]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = even_number_filter(numbers)
for num in even_nums:
    print(num)

