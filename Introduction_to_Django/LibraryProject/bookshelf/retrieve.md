# Retrieve Operation

from bookshelf.models import Book

# Retrieving the book
book = Book.objects.get(id=1)

print(f"Title: {book.title}")  # Expected Output: Title: 1984
print(f"Author: {book.author}")  # Expected Output: Author: George Orwell
print(f"Publication Year: {book.publication_year}")  # Expected Output: Publication Year: 1949
