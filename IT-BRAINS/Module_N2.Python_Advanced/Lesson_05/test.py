# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# # for key in my_dict:
# #     value = my_dict[key]
# #     print(key, ":", value)
# #
# #
# # for key in my_dict:
# #     print(key)
#
# ww = my_dict.keys()
# print(ww)

# a = "123456"
# b = 2
# c = 4
# d = c * b
# print(d)

class EvenRangeIterator:
    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end
        self.current = self.start if self.start % 2 == 0 else self.start + 1

#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         even_num = self.current
#         self.current += 2
#         return even_num
#
#
# even_nums = EvenRangeIterator(1, 10)
# for num in even_nums:
#     print(num)



class EvenRangeIterator:
    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end
        self.current = self.start if self.start % 2 == 0 else self.start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        even_num = self.current
        self.current += 2
        return even_num


even_nums = EvenRangeIterator(3, 10)
for num in even_nums:
    print(num)

