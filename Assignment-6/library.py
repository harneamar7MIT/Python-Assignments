class Library:
    
    # Constructor
    def __init__(self, books):
        self.available_books = books
        self.borrowed_books = []

    # Display books
    def display(self):
        print("\nAvailable Books:")
        if len(self.available_books) == 0:
            print("No books available.")
        else:
            for book in self.available_books:
                print("-", book)

    # Checkout book
    def checkout(self, book_name):
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.borrowed_books.append(book_name)
            print(f"You have successfully borrowed '{book_name}'.")
        else:
            print(f"Sorry, '{book_name}' is not available.")

    # Return book
    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            self.available_books.append(book_name)
            print(f"You have successfully returned '{book_name}'.")
        else:
            print(f"'{book_name}' was not borrowed from this library.")


# Creating Library object
books_list = ["Python Basics", "Data Structures", "Machine Learning", "AI Fundamentals"]
library = Library(books_list)

# Using methods
library.display()
library.checkout("Python Basics")
library.display()
library.return_book("Python Basics")
library.display()