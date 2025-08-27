
# Assignment 1: My Own Class

# A Book class with details about a book and methods to do with reading

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Method 1: read the book
    def read(self):
        return f"Reading '{self.title}' by {self.author} 📖"

    # Method 2: check book length
    def length(self):
        if self.pages > 300:
            return f"{self.title} is a long book."
        else:
            return f"{self.title} is a short book."


# Creating book objects
book1 = Book("Things Fall Apart", "Chinua Achebe", 209)
book2 = Book("Harry Potter", "J.K. Rowling", 500)

# Trying out the methods
print(book1.read())
print(book1.length())

print(book2.read())
print(book2.length())
