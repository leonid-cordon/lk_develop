# Module 2, Lecture 5, Homework 9
# Create an iterator that iterates over all palindromes (words that read the same
# from left to right and right to left) from a given list of words.

class PalindromeIterator:

    def __init__(self, word_list: list):
        """
        Initialize the PalindromeIterator with a list of words.

        Args:
            word_list (list): The list of words.
        """
        self.word_list = word_list
        self.index = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next palindrome from the word list.

        Returns:
            str: The next palindrome.

        Raises:
            StopIteration: If there are no more palindromes in the word list.
        """
        while self.index < len(self.word_list):
            _word = self.word_list[self.index]
            self.index += 1
            if _word == _word[::-1]:
                return _word
        raise StopIteration


# Example of calling and outputting the result
words_list = ['level', 'racecar', 'python', 'madam']
palindrome_iter = PalindromeIterator(words_list)
for word in palindrome_iter:
    print(word)
