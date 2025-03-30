from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from rest_framework.permissions import IsAuthenticated

class NotificationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(recipient=user, is_read=False)
        data = [{"actor": notification.actor.username, "verb": notification.verb, "target": str(notification.target), "timestamp": notification.timestamp} for notification in notifications]
        return Response(data, status=status.HTTP_200_OK)

class MarkAsRead(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, notification_id):
        user = request.user
        try:
            notification = Notification.objects.get(id=notification_id, recipient=user)
            notification.is_read = True
            notification.save()
            return Response({"message": "Notification marked as read."}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({"message": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)

