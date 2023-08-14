# Module 2, Lecture 3, Homework 5

# Develop a class Library to represent a library.
# Also, create a class Book to represent a book.
# The Library class should have an attribute called "books" as a list of books.
# Each book in the library should have attributes such
# as title, author, and publication year.
# Implement the add_book method, which adds a new book to the library.
# Implement the str method, which displays the list of books in the library.
# Create an object of Library and add some books. Print the list of books in the library.
class Library:
    def __init__(self, books):
        """
        Initializes a Library object.

        Args:
            books (list): A list of Book objects representing the books in the library.
        """
        self.books = books

    def add_book(self, new_book):
        """
        Adds a new book to the library.

        Args:
            new_book (Book): A Book object representing the new book to be added.
        """
        self.books.append(new_book)

    def __str__(self):
        """
        Returns a string representation of the Library object.

        Returns:
            str: A formatted string displaying the list of books in the library.
        """
        # (str(book) for book in self.books) to convert each book object in self.books into a string
        book_list = "\n".join(str(book) for book in self.books)
        return f"List of books in Library:\n{book_list}"


class Book:
    def __init__(self, title, author, publication_year):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The year of publication of the book.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        """
        Returns a string representation of the Book object.

        Returns:
            str: A formatted string displaying the details of the book.
        """
        return f"{self.title} by {self.author}, {self.publication_year}"


book_01 = Book("To Kill a Mockingbird",  "Harper Lee", 1960)
book_02 = Book("Harry Potter and the Philosopher's Stone", "J.K.Rowling", 1997)
book_03 = Book("The Lord of the Rings", "J.R.R.Tolkien", 1954)
book_04 = Book("The Da Vinci Code", "Dan Brown", 2003)
book_05 = Book("The Alchemist", "Paulo Coelho", 1988)

library = Library([book_01, book_02, book_03, book_04, book_05])
book_06 = Book("1984", "George Orwell", 1949)

library.add_book(book_06)

print(library)
