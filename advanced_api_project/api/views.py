from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
import logging
from .models import Book
from .serializers import BookSerializer

# Set up logging
logger = logging.getLogger(__name__)

# List all books (Public access)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'genre']

# Retrieve a single book by ID (Public access)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book (Restricted to authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f"New book '{serializer.validated_data['title']}' created.")

# Update an existing book (Restricted to authenticated users)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f"Book '{serializer.validated_data['title']}' updated.")

# Delete a book (Restricted to authenticated users)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
