from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Only import BookViewSet now

# Create a router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Include the router URLs for CRUD operations
    path('', include(router.urls)),
]
