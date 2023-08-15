# Module 2, Lecture 3, Homework 8

#   Create a class called "Book" that has the following attributes:
#  "year", "title", "author", and "page_count".
#  Create a static method that takes a list of books and a year
#  as input and returns the number of books from that list that were published in that year.

class Book:
    def __init__(self, year, title, author, page_count):
        """
        Initialize a Book instance with the provided attributes.

        Args:
            year (int): The year of publication.
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The number of pages in the book.
        """
        self.year = year
        self.title = title
        self.author = author
        self.page_count = page_count

    @staticmethod
    def count_books_by_year(book_list_input, year):
        """
        Count the number of books in the given list that were published in the specified year.

        Args:
            book_list_input (list): A list of Book instances.
            year (int): The year to count the books for.

        Returns:
            int: The number of books published in the given year.
        """
        count = 0
        for book in book_list:
            if book.year == year:
                count += 1
        return count


book_list = [
    Book(2001, "Title 01", "Author 01", 101),
    Book(2002, "Title 02", "Author 02", 102),
    Book(2003, "Title 03", "Author 03", 103),
    Book(2002, "Title 04", "Author 04", 104)
]

target_year = 2002
output = Book.count_books_by_year(book_list, target_year)
print(f"Number of books published in the year {target_year}: {output}")
