# Module 2, Lecture 5, Homework 7
# Create an iterator that iterates over all even numbers within a given range.
class EvenRangeIterator:
    def __init__(self, _start, _end):
        """
        Initializes the EvenRangeIterator object.

        Args:
            _start (int): The starting value of the range.
            _end (int): The ending value of the range.
        """
        self.start = _start
        self.end = _end
        self.current = self.start if self.start % 2 == 0 else self.start + 1

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            EvenRangeIterator: The iterator object.
        """
        return self

    def __next__(self):
        """
        Returns the next even number in the range.

        Returns:
            int: The next even number.

        Raises:
            StopIteration: If there are no more even numbers in the range.
        """
        if self.current > self.end:
            raise StopIteration
        even_num = self.current
        self.current += 2
        return even_num


even_nums = EvenRangeIterator(5, 15)
for num in even_nums:
    print(num)