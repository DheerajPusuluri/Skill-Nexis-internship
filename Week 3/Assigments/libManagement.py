class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(book, "has been added.")
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "has been removed.")
        else:
            print(book, "is not available in the library.")
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "has been issued.")
        else:
            print(book, "is not available.")
    def return_book(self, book):
        self.books.append(book)
        print(book, "has been returned.")
    def display_books(self):
        if self.books:
            print("Available Books:")
            for book in self.books:
                print("-", book)
        else:
            print("No books are available.")
library = Library()
library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning")
library.display_books()
library.issue_book("Python Programming")
library.display_books()
library.return_book("Python Programming")
library.remove_book("Data Structures")
library.display_books()