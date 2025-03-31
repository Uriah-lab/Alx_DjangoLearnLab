# Update Operation

from bookshelf.models import Book

# Updating the title
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

print(book)  # Expected Output: Nineteen Eighty-Four by George Orwell (1949)
