from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the list of users that the current user follows
        followed_users = request.user.following.all()
        posts = Post.objects.filter(user__in=followed_users).order_by('-created_at')

        # Serialize the posts
        post_data = PostSerializer(posts, many=True).data

        return Response(post_data)
