# Retrieve Operation for Book Model

In this step, we retrieve the created book from the database.

```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
