from django.shortcuts import render

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# BookViewSet is restricted to authenticated users, only those with valid tokens can access this API.
# To obtain a token, use the /api-token-auth/ endpoint by passing your username and password.
# After authentication, the token must be included in the Authorization header as:
# Authorization: Token <your_token>