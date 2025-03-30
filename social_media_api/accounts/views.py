from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view

User = get_user_model()

@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    user = request.user  # Assuming request.user is authenticated

    # Add the user to the following list of the current user
    user.following.add(user_to_follow)
    return JsonResponse({"message": "Followed successfully"})

@api_view(['DELETE'])
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    user = request.user  # Assuming request.user is authenticated

    # Remove the user from the following list of the current user
    user.following.remove(user_to_unfollow)
    return JsonResponse({"message": "Unfollowed successfully"})
