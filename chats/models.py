from django.db import models
from django.conf import settings

class Chat(models.Model):
    user            = models.CharField(max_length=100)
    message         = models.TextField()
    attachment_name = models.TextField()
    is_sent         = models.SmallIntegerField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user