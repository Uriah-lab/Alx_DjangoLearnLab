# Retrieve a Book Instance

## Command:
```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
```python
book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id).title)