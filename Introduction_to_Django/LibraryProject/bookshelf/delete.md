# Delete a Book Instance

## Command:
```python
book.delete()
print(Book.objects.all())  # Should return an empty queryset
<QuerySet []>
After documenting each operation separately, you can **combine them into one master file**:

```bash
cat create.md retrieve.md update.md delete.md > CRUD_operations.md