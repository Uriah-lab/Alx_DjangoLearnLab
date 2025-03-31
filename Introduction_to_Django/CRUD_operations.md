# CRUD Operations for the Book Model

##  Create Operation

```python
from bookshelf.models import Book

# Creating a Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

print(book)  # Expected Output: 1984 by George Orwell (1949)

from bookshelf.models import Book

# Retrieving the book
book = Book.objects.get(id=1)

print(f"Title: {book.title}")  # Expected Output: Title: 1984
print(f"Author: {book.author}")  # Expected Output: Author: George Orwell
print(f"Publication Year: {book.publication_year}")  # Expected Output: Publication Year: 1949

from bookshelf.models import Book

# Updating the title
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

print(book)  # Expected Output: Nineteen Eighty-Four by George Orwell (1949)

from bookshelf.models import Book

# Deleting the book
book = Book.objects.get(id=1)
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)  # Expected Output: <QuerySet []>
