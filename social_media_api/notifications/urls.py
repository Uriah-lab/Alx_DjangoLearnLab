from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.NotificationList.as_view(), name='notification_list'),
    path('notifications/<int:notification_id>/read/', views.MarkAsRead.as_view(), name='mark_as_read'),
]
