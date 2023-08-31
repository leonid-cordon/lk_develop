# Module 2, Lecture 5, Homework 5
# Implement an iterator to iterate over all keys of a dictionary.

class DictKeysIterator:
    """
    An iterator for iterating over all keys of a dictionary.
    """

    def __init__(self, input_dict: dict):
        """
        Initializes the DictKeysIterator with the provided input dictionary.

        :param input_dict: The dictionary to iterate over.
        """
        self._dict = input_dict
        self._keys = list(input_dict.keys())
        self._index = 0

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next key from the dictionary on each call.
        Raises StopIteration when all keys have been iterated.
        """
        if self._index >= len(self._keys):
            raise StopIteration
        else:
            _key = self._keys[self._index]
            self._index += 1
            return _key


# Example usage and output
dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = DictKeysIterator(dictionary)
for key in dict_iter:
    print(key)

