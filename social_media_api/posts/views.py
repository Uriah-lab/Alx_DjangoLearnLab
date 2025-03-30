from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like
from notifications.models import Notification
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from notifications.models import Notification

class LikePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        post = Post.objects.get(pk=pk)

        # Prevent multiple likes by the same user on the same post
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a like
        Like.objects.create(user=user, post=post)

        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked your post",
            target=post
        )

        return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePost(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        user = request.user
        post = Post.objects.get(pk=pk)

        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "Like not found."}, status=status.HTTP_400_BAD_REQUEST)
