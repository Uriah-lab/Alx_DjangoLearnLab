from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/like/', views.LikePost.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', views.UnlikePost.as_view(), name='unlike_post'),
]
