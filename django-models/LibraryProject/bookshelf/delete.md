# Delete Operation

from bookshelf.models import Book

# Deleting the book
book = Book.objects.get(id=1)
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)  # Expected Output: <QuerySet []>
