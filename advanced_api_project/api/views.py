from django.shortcuts import render

from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of authors or create a new author.
    Uses the AuthorSerializer to handle serialization.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific author.
    Supports GET, PUT, PATCH, and DELETE requests.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    API view to retrieve a list of books or create a new book.
    Uses the BookSerializer and ensures books link to existing authors.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific book.
    Supports GET, PUT, PATCH, and DELETE requests.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

