# CRUD Operations for Book Model

## 1. Create Operation - `create.md`
In this step, we create a book instance in the Django shell.

```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
