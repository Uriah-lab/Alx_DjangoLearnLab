# Update a Book Instance

## Command:
```python
book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id).title)
Nineteen Eighty-Four
```python
book.delete()
print(Book.objects.all())  # Should return an empty queryset