import os
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Retrieve all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")

# Query 2: List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name} Library:")
    for book in books:
        print(f"- {book.title}")

# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name} Library: {librarian.name}")

# Run Sample Queries
if __name__ == "__main__":
    # Ensure sample data is created first!
    books_by_author("J.K. Rowling")
    books_in_library("Central Library")
    librarian_for_library("Central Library")
