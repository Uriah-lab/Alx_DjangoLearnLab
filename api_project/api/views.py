from django.shortcuts import render

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
