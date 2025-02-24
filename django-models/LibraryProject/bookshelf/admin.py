from django.contrib import admin

from .models import Book
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters to the admin panel
    list_filter = ('author', 'publication_year')
    
    # Add search capabilities for the title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)