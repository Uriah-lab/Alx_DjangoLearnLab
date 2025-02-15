# Django Admin Configuration for Book Model

## Steps Followed:
1. Registered the `Book` model in `bookshelf/admin.py`.
2. Added `list_display` to show Title, Author, and Publication Year.
3. Implemented `search_fields` for searching by title and author.
4. Configured `list_filter` to filter books by publication year.
5. Created a superuser using `python3 manage.py createsuperuser`.
6. Tested the admin panel at `http://127.0.0.1:8000/admin/`.

## Expected Outcome:
- Books can be added, edited, and deleted via Django Admin.
- Search and filtering functionalities work correctly.