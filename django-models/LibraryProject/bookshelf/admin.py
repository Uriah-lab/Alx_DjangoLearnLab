from django.contrib import admin
from .models import Book

# Customize Admin Interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display in list view
    search_fields = ('title', 'author')  # Search by title and author
    list_filter = ('publication_year',)  # Filter by publication year

# Register the model
admin.site.register(Book, BookAdmin)

