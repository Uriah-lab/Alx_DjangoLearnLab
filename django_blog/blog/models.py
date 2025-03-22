from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/posts/{self.id}/"



