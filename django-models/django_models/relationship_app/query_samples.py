from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(book.title)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name}: {librarian.name}")

# Sample function calls for testing
if __name__ == "__main__":
    # Test each query
    books_by_author("J.K. Rowling")
    books_in_library("City Library")
    librarian_for_library("City Library")
