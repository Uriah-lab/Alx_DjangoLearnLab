# Create a Book Instance

## Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
<Book: 1984>
```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)